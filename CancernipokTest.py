import subprocess
import tempfile
import time
import random
import string
import os

selftext=open(__file__,"r").read()

dirpath="/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs"
for x in xrange (200):
    newfile=tempfile.NamedTemporaryFile("w", dir=dirpath, delete=False)
    imax=len(selftext)
    randomsteps=random.randint(0,20)
    newtext=selftext

    for i in xrange (randomsteps):
        characters = string.printable
        y=random.choice(characters)

        change = random.randint(0,imax)

        newtext = newtext[:change]+y+newtext[change+1:]

    newfile.write(newtext)
    newfile.close()

    #testcode = subprocess.Popen(["python", newfile.name])

    #time.sleep(.5)

    #if testcode.poll() and testcode.returncode != 0:
        #os.remove(newfile.name)
