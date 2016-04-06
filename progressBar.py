from __future__ import division
import sys, time, os

progress=0

def update_progress(progress):
    barLength = 100 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rProgress: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


progArray=[]

while True:
    progressPaths=os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Progress Storage"))
    progressPaths=progressPaths[1:]
    for path in progressPaths:
        progPath=os.path.join(os.path.dirname(os.path.abspath(path)),"Progress Storage", path)
        with open(progPath) as storeEx:
            prog=(storeEx.read())
        if prog:
            prog=float(prog)
        else:
            prog=0
        progArray.append(prog)

    progArray.sort()
    try:
        progress=progArray[-1]
    except:
        progress=0
        pass
    update_progress((progress/100))
    if progress==100:
        break
    time.sleep(.1)
