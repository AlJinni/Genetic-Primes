import os, shutil

primeFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Clone Wars")
bestFiles=[]
dirGens=[]

def TEST():
    for direc in os.listdir(primeFolder)[1:]:
        dirGens.append(int(direc[4:]))
        dirGens.sort()
        targetGen=dirGens[-1]

        

def PURGE():
    print ""
    for prime in os.listdir(primeFolder):
        filePath = os.path.join(primeFolder, prime)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath): shutil.rmtree(filePath)
        except Exception as e:
            print(e)
