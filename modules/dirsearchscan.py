import conf.conf as conf
from os.path import expanduser

def dirsearchScan() :
    print("===================================================================")
    print( conf.colored(conf.text2art ("Dirsearch Scan", "small"),'cyan'))
    print("===================================================================")

    dirTarget = input( conf.colored("\nEnter target: ", "green", attrs=['bold']))
    dirOutput = input( conf.colored(f"Enter the output folder - [default: reports/Dirsearch/{dirTarget}/]: ","green", attrs=['bold']))

    conf.notValid(dirsearchScan, dirTarget)
    dirOutput = conf.dirOutput(dirOutput, "reports/Dirsearch", dirTarget)
    conf.createDir(dirOutput)

    home = expanduser("~")
    conf.os.system(f"python3 {home}/.opt/dirsearch/dirsearch.py -u {dirTarget} --simple-report={dirOutput}/dirsearch.txt")

    print("______________________________________________________________________")
