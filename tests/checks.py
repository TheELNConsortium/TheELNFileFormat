import json
import traceback
import tempfile
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from jsonschema import Draft202012Validator
from rocrate.rocrate import ROCrate
from rocrate_validator import services, models

METADATA_FILE = 'ro-crate-metadata.json'


def checkArchiveStructure(fileName):
    """Check that an .eln ZIP contains exactly one root folder.

    Args:
        fileName: path to .eln file
    Returns:
        success: bool if check was successful
        log: string with log information
    """
    with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        entries_outside_root = set()
        root_folders = set()
        for entry in elnFile.infolist():
            path = PurePosixPath(entry.filename)
            if (
                    not path.parts
                    or path.is_absolute()
                    or '..' in path.parts
                    or (len(path.parts) == 1 and not entry.is_dir())
            ):
                entries_outside_root.add(entry.filename)
            else:
                root_folders.add(path.parts[0])

        log = ''
        if entries_outside_root:
            entries = ', '.join(
                repr(path) for path in sorted(entries_outside_root)
            )
            log += (
                '**ERROR: .eln archive entries must be stored inside the root '
                f'folder: {entries}\n'
            )
        if len(root_folders) != 1:
            folders = ', '.join(repr(path) for path in sorted(root_folders))
            log += (
                '**ERROR: .eln archive must contain exactly one root folder; '
                f'found {len(root_folders)}: {folders}\n'
            )
        return not log, log


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
        node_types = node['@type']
        if isinstance(node_types, str):
            node_types = [node_types]
        elif not isinstance(node_types, list):
            node_types = []
        if 'Dataset' in node_types:
            for key in DATASET_MANDATORY:
                if key not in node:
                    print(f'**ERROR in dataset: "{key}" not in @id={node["@id"]}')
                    globalSuccess = False
            for key in DATASET_SUGGESTED:
                if key not in node and OUTPUT_INFO:
                    print(f'**INFO for dataset: "{key}" not in @id={node["@id"]}')
        elif 'File' in node_types:
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
            log += f'- {error.message}\n'
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
        if metadataNode.get('sdPublisher',{}).get('@id','') in ['SampleDB', 'https://github.com/paulscherrerinstitute/scilog']:
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


ALL_CHECKS = (
    ('Archive structure', checkArchiveStructure),
    ('Pypi RO-Crate', checkPypiRocrate),
    ('Parameters metadata json', checkParamMetadataJson),
    ('Schema', checkSchema),
    ('Validator', checkValidator),
)


def readUploadedBytes(uploadedFile):
    """ Read the raw bytes of an uploaded .eln file
    Args:
        uploadedFile: bytes, or a file-like object such as a web upload
    Returns:
        payload: bytes of the .eln file
    """
    if isinstance(uploadedFile, (bytes, bytearray)):
        return bytes(uploadedFile)
    if hasattr(uploadedFile, 'getvalue'):
        return uploadedFile.getvalue()
    if hasattr(uploadedFile, 'seek'):
        uploadedFile.seek(0)
    return uploadedFile.read()


@contextmanager
def uploadedFileAsPath(uploadedFile, fileName='uploaded.eln'):
    """ Expose an uploaded .eln file object as a real file on disk

    Most checks accept any file-like object, but checkValidator resolves
    Path(fileName).parent.name and therefore needs a real path. Writing the
    upload out once keeps all five checks on one identical input instead of
    letting them disagree about what they received.

    Args:
        uploadedFile: bytes, or a file-like object such as a web upload
        fileName: name to give the temporary copy; only its basename is used
    Yields:
        elnPath: Path of the temporary .eln file, removed on exit
    """
    payload = readUploadedBytes(uploadedFile)
    with tempfile.TemporaryDirectory() as directory:
        elnPath = Path(directory)/'upload'/Path(fileName).name
        elnPath.parent.mkdir(parents=True, exist_ok=True)
        elnPath.write_bytes(payload)
        yield elnPath


@contextmanager
def _asPath(source, fileName=None):
    """ Yield a filesystem path for either a real path or an uploaded object

    When *source* is an existing file path it is used directly. Any other
    object (bytes, BytesIO, Streamlit UploadedFile, ...) is materialised to a
    temporary file via :func:`uploadedFileAsPath` so every check receives one
    identical on-disk input and the temporary-file handling stays inside the
    validation code.

    Args:
        source: a filesystem path (str/Path) or an uploaded file object
        fileName: name for the temporary copy when *source* is an upload
    Yields:
        elnPath: Path of the .eln file to check
    """
    if isinstance(source, (str, Path)) and Path(source).is_file():
        yield Path(source)
    else:
        with uploadedFileAsPath(source, fileName or 'uploaded.eln') as elnPath:
            yield elnPath


def runChecks(source, fileName=None):
    """ Run every .eln check against a file path or an uploaded file object

    Both the CI test suite and the Streamlit web app call this single entry
    point so the web tool and the CI suite always agree about what a valid
    .eln file is. A check that raises is reported as a failure rather than
    propagating, because reporting on damaged files is the purpose of an
    upload tool.

    Args:
        source: a filesystem path (str or Path) to an .eln file, or an
            uploaded file object (bytes, BytesIO, Streamlit UploadedFile, ...)
        fileName: name to give a temporary copy when *source* is an upload;
            only its basename is used and defaults to ``uploaded.eln``.
            Ignored when *source* is an existing path.
    Returns:
        results: list of (label, success, log) in ALL_CHECKS order
    """
    results = []
    with _asPath(source, fileName) as elnPath:
        for label, check in ALL_CHECKS:
            try:
                success, log = check(elnPath)
            except Exception:
                success = False
                log = '  *****  ERROR: this check could not run on the file  *****\n'
                log += traceback.format_exc()
            results.append((label, success, log))
    return results


def checkUploadedFile(uploadedFile, fileName='uploaded.eln'):
    """ Backward-compatible alias for :func:`runChecks` with an upload object """
    return runChecks(uploadedFile, fileName)
