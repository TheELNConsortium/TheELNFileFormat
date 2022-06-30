#!/usr/bin/python3
import os, shutil, json, sys
from zipfile import ZipFile, ZIP_DEFLATED

def simplify(metadata):
  """
  simplify metadata by removing everything except @id, @type, hasPart
  """
  for item in metadata['@graph']:
    if item['@id'] in ['ro-crate-metadata.json','./']:
      continue
    for subitem in [i for  i in item]:
      if subitem not in ['@id','@type','hasPart']:
        del item[subitem]
  return json.dumps(metadata, indent=2)


def tree(metadata):
  def processPart(part, level):
    """
    recursive function call to process this node
    """
    prefix = '    '*(level-1)+'|-> '
    output = prefix+part['@id']+'\n'
    # find next node to process
    newNode = [i for i in metadata['@graph'] if '@id' in i and i['@id']==part['@id']]
    if len(newNode)==1:
      newNode = newNode[0]
      subparts = newNode.pop('hasPart') if 'hasPart' in newNode else []
      if len(subparts)>0:  #don't do if no subparts: measurements, ...
        for subpart in subparts:
          output += processPart(subpart, level+1)
    return output

  ######################
  #main tree-function
  graph = metadata["@graph"]
  #find information from master node
  rocrateNode = [i for i in graph if i["@id"]=="ro-crate-metadata.json"][0]
  output = 'ro-crate-metadata.json\n'
  if 'sdPublisher' in rocrateNode:
    output += rocrateNode['sdPublisher']['name']+'\n'
  if 'version' in rocrateNode:
    output += rocrateNode['version']+'\n'
  mainNode    = [i for i in graph if i["@id"]=="./"][0]
  output += './\n'
  #iteratively go through list
  for part in mainNode['hasPart']:
    output += processPart(part, 1) #TODO_P2 first child should get elnName and version
  return output


if __name__ == '__main__':
  #prepare README.md file
  if os.path.exists('README_template.md'):
    shutil.copy('README_template.md','README.md')
  outfile = open('README.md','a')

  for fileName in os.listdir('.'):
    if fileName.endswith('.eln'):
      outfile.write('\n### '+fileName+'\n')
      with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
        files = elnFile.namelist()
        dirName=files[0].split(os.sep)[0]
        if dirName+'/ro-crate-metadata.json' in files:
          metadata = json.loads(elnFile.read(dirName+'/ro-crate-metadata.json'))
          if len(sys.argv)>1 and sys.argv[1]=='simple':
            output = simplify(metadata)
          if len(sys.argv)>1 and sys.argv[1]=='tree':
            output = tree(metadata)
          else:
            output = json.dumps(metadata, indent=2)
          outfile.write('```\n'+output+'\n```\n\n')
  outfile.close()

