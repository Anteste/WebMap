import conf.conf as conf

def niktoScan() :
    print("==============================================")
    print( conf.colored(conf.text2art ("Nikto Scan", "small"),'cyan'))
    print("==============================================")

    niktoTarget = input( conf.colored("\nEnter target: ", "green", attrs=['bold']))
    niktoOutput = input( conf.colored(f"Enter the output folder - [default: reports/Nikto/{niktoTarget}/]: ","green", attrs=['bold']))

    conf.notValid(niktoScan, niktoTarget)
    niktoOutput = conf.dirOutput(niktoOutput, "reports/Nikto", niktoTarget)

    conf.createDir(niktoOutput)

    conf.os.system(f"nikto +h {niktoTarget} -output {niktoOutput}/nikto.txt") 
    
    print("______________________________________________________________________")
