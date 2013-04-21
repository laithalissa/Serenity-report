import os
from os import path, system

inputExt = ".tiff"
outputExt = ".pdf"
cmd = "convert"

def main():
    pwd = os.getcwd()

    fileNames = [qualify(pwd,file) for file in os.listdir(pwd) if path.isfile(qualify(pwd, file)) and file.endswith(inputExt)]
    fileNameMap = {n: swapExt(n) for n in fileNames}
    for inFile, outFile in fileNameMap.items():
	if not system("%s '%s' '%s'" % (cmd, inFile, outFile)):
	    system("rm '%s'" % inFile)
	
    
def qualify(parent, child):
    return parent + os.sep + child

def swapExt(fileName):
    return fileName.replace(inputExt, outputExt) if fileName.endswith(inputExt) else fileName

main()
