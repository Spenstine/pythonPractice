import os

def search(dirname):
    List = []
    for names in os.listdir(dirname):
        path = os.path.join(dirname, names)
        if os.path.isfile(path):
            if path.endswith('.mp3'):
                List.append(path)
        else:
            search(path)
    return List

def find_checksum(anylist):
    sipeDict = {}
    for item in anylist:
        item = item.split()
        item.append('"')
        item.insert(0, '"')
        item = "".join(item)
        cmd = 'md5sum ' + item
        fp = os.popen(cmd)
        searchList = fp.read().split()
        if len(searchList) > 1:
            sipeDict[item] = searchList[0]
        fp.close()
    return sipeDict

def findDuplicates(checksumDict):
    checkValues = list(checksumDict.values())
    checkKeys = list(checksumDict.keys())
    for keys,values in checksumDict.items():
        for i in range(len(checkValues)):
            if values == checkValues[i] and keys != checkKeys[i]:
                print("Duplicates: ", keys, checkKeys[i])

fileList = search('../music/WhatsApp Audio')
checkDict = find_checksum(fileList)
findDuplicates(checkDict)