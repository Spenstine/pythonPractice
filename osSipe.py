import os

def search(dirname):
    musicList = []
    for names in os.listdir(dirname):
        path = os.path.join(dirname, names)
        if os.path.isfile(path):
            if path.endswith('.mp3'):
                musicList.append(path)
        else:
            search(path)

def findDuplicates(anylist):
    for item in anylist:
        cmd1 = 'md5sum ' + item
        fp1 = os.popen(cmd1)
        for i in range(len(anylist)):
            cmd2 = 'md5sum ' + anylist[i]
            fp2 = os.popen(cmd2)
            if fp1 == fp2:
                print("duplicates: ", item, anylist[i])
    fp1.close()
    fp2.close()
search('.')