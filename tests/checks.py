import json
import traceback
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from jsonschema import Draft202012Validator
from rocrate.rocrate import ROCrate
from rocrate_validator import services, models

METADATA_FILE = 'ro-crate-metadata.json'

def checkPypiRocrate(fileName, verbose=False):
    """ Check if file is a valid ro-crate according to pypi rocrate package
    https://pypi.org/project/rocrate/
    Args:
        fileName: path to .eln file
        verbose: bool if verbose output should be generated
    Returns:
        success: bool if check was successful
        log: string with log information
    """
    with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        try:
            dirpath = Path(tempfile.mkdtemp())
            elnFile.extractall(dirpath)
            tempPath= [i for i in dirpath.iterdir() if i.is_dir()][0]
            crate = ROCrate(tempPath)
            log = ""
            for e in crate.get_entities():
                if verbose:
                    log+= f'  {e.id}: {e.type}\n'
            return True, log
        except Exception:
            log = "  *****  ERROR: Could not parse content of this file!!  *****\n"
            log+= f"  Temporary folder: {tempPath}\n"
            log+= traceback.format_exc()
            return False, log


def checkParamMetadataJson(fileName):
    """ Check if file is a valid ro-crate according to pypi rocrate package
    Args:
        fileName: path to .eln file
    Returns:
        success: bool if check was successful
        log: string with log information
    """
    # global variables worth discussion
    ROCRATE_NOTE_MANDATORY = ['version','sdPublisher']
    DATASET_MANDATORY = ['name']
    DATASET_SUGGESTED = ['author','mentions',  'dateCreated', 'dateModified', 'identifier', 'text', 'keywords']
    FILE_MANDATORY = ['name']
    FILE_SUGGESTED = ['sha256', 'encodingFormat', 'contentSize', 'description']

    # runtime global variables
    OUTPUT_INFO = False
    OUTPUT_COUNTS = False
    KNOWN_KEYS = DATASET_MANDATORY+DATASET_SUGGESTED+FILE_MANDATORY+FILE_SUGGESTED+['@id', '@type']

    def processNode(graph, nodeID):
        """
        recursive function call to process each node

        Args:
            graph: full graph
            nodeID: id of node in graph
        """
        globalSuccess = True
        nodes = [ i for i in graph if '@id' in i and i['@id'] == nodeID]
        if len(nodes)!=1:
            print('**ERROR: all entries must only occur once in crate. check:', nodeID)
            return
        node = nodes[0]
        # CHECK IF MANDATORY AND SUGGESTED KEYWORDS ARE PRESENT
        if '@type' not in node:
            print('**ERROR: all nodes must have @type. check:', nodeID)
            return False
        if node['@type'] == 'Dataset':
            for key in DATASET_MANDATORY:
                if key not in node:
                    print(f'**ERROR in dataset: "{key}" not in @id={node["@id"]}')
                    globalSuccess = False
            for key in DATASET_SUGGESTED:
                if key not in node and OUTPUT_INFO:
                    print(f'**INFO for dataset: "{key}" not in @id={node["@id"]}')
        elif node['@type'] == 'File':
            for key in FILE_MANDATORY:
                if key not in node:
                    print(f'**ERROR in file: "{key}" not in @id={node["@id"]}')
                    globalSuccess = False
            for key in FILE_SUGGESTED:
                if key not in node and OUTPUT_INFO:
                    print(f'**INFO for file: "{key}" not in @id={node["@id"]}')
        # CHECK PROPERTIES FOR ALL KEYS
        if any(not str(i).strip() for i in node.values()):
            print(f'**WARNING: {nodeID} contains empty values in the key-value pairs')
        # SPECIFIC CHECKS ON CERTAIN KEYS
        if isinstance(node.get('keywords', ''), list):
            print(f'**ERROR: {nodeID} contains an array of keywords. Use comma or space separated string')
            globalSuccess = False
        # recurse to children
        children = node.pop('hasPart') if 'hasPart' in node else []
        for child in children:
            globalSuccess = processNode(graph, child['@id']) and globalSuccess
        return globalSuccess

    success = True
    log = ''
    with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        success = True
        metadataJsonFile = [i for i in elnFile.namelist() if i.endswith(METADATA_FILE)][0]
        metadataContent = json.loads(elnFile.read(metadataJsonFile))
        graph = metadataContent["@graph"]
        # find information from master node
        ro_crate_nodes = [i for i in graph if i["@id"] == METADATA_FILE]
        if len(ro_crate_nodes) == 1:
            for key in ROCRATE_NOTE_MANDATORY:
                if key not in ro_crate_nodes[0]:
                    log += f'**ERROR: "{key}" not in @id={METADATA_FILE}'
        else:
            log += f'**ERROR: @id={METADATA_FILE} does not uniquely exist '
            success = False
        main_node = [i for i in graph if i["@id"] == "./"][0]

        # iteratively go through graph
        for partI in main_node['hasPart']:
            success = processNode(graph, partI['@id']) and success

        # count occurances of all keys
        counts = {}
        for node in graph:
            if node['@id'] in ['./',METADATA_FILE]:
                continue
            for key in node.keys():
                if key in counts:
                    counts[key] += 1
                else:
                    counts[key] = 1

        view = [ (v,k) for k,v in counts.items() ]
        view.sort(reverse=True)
        if OUTPUT_COUNTS:
            log += '===== Counts (* unspecified)'
            for v,k in view:
                prefix = '   ' if k in KNOWN_KEYS else ' * '
                log += f'{prefix}{k:15}: {v}'
    return success, log


def checkSchema(fileName):
    """ Check if file is a valid ro-crate according to THE-ELN-Consortium schema
    Args:
        fileName: path to .eln file
    Returns:
        success: bool if check was successful
        log: string with log information
    """
    log = ''
    schema = json.load(open(Path(__file__).parent/'schema.json', 'r', encoding='utf-8'))
    validator = Draft202012Validator(schema=schema)
    validator.check_schema(schema=schema)
    success = True
    with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        metadataJsonFile = [i for i in elnFile.namelist() if i.endswith(METADATA_FILE)][0]
        metadataContent = json.loads(elnFile.read(metadataJsonFile))
        for error in sorted(validator.iter_errors(metadataContent), key=str):
            log += f'- {error.message}'
            success = False
    return success, log


def checkValidator(fileName):
    """ Check if file is a valid ro-crate according to rocrate-validator
    Args:
        fileName: path to .eln file
    Returns:
        success: bool if check was successful
        log: string with log information
    """
    log = ''
    success = True
    with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        dirpath = Path(tempfile.mkdtemp())/Path(fileName).parent.name
        dirpath.mkdir(parents=True, exist_ok=True)
        elnFile.extractall(dirpath)
        rocrate_dir= [i for i in dirpath.iterdir() if i.is_dir()][0]

        # short stop-gap measure because the validator currently does not support the latest ro-crate version
        with open(rocrate_dir/METADATA_FILE, 'r', encoding='utf-8') as f:
            metadata = f.read()
        # SampleDB
        metadataNode = [i for i in json.loads(metadata)['@graph'] if i['@id']==METADATA_FILE][0]
        if metadataNode.get('sdPublisher',{}).get('@id','')=='SampleDB':
            metadata = metadata.replace('"@id": "https://w3id.org/ro/crate/1.2"','"@id": "https://w3id.org/ro/crate/1.1"')
        # eLabFTW
        publisherNodes = [i for i in json.loads(metadata)['@graph'] if i['@id']=='#publisher']
        if len(publisherNodes)==1 and publisherNodes[0].get('name','')=='eLabFTW':
            metadata = metadata.replace('conformsTo":{"@id":"https:\/\/w3id.org\/ro\/crate\/1.2"}',
                                        'conformsTo":{"@id":"https:\/\/w3id.org\/ro\/crate\/1.1"}')
        # finish
        with open(rocrate_dir/METADATA_FILE, 'w', encoding='utf-8') as f:
            f.write(metadata)

        # start validation
        settings = services.ValidationSettings(
            rocrate_uri=rocrate_dir,
            profile_identifier='ro-crate-1.1',
            requirement_severity=models.Severity.REQUIRED,
        )
        result = services.validate(settings) # this step takes time
        if result.has_issues():
            log += f'{fileName} is not valid\n'
            for issue in result.get_issues():
                log += f"Detected issue of severity {issue.severity.name} with check \"{issue.check.identifier}\": {issue.message}\n"
            success = False
    return success, log
