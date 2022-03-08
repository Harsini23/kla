import yaml
from datetime import datetime, timedelta
now = datetime.now()
with open(r'C:\Users\ramal\OneDrive\Desktop\kla\test.yaml') as file:
    service = yaml.safe_load(file)

    def seqfunction(activity, name, file1, recurname):
        global now
        # ~file1 = open("klaout.txt", "w")
        for key in activity:
            currobj = activity[key]
            if(recurname == "None"):
                printobj = ";" + name+"."+key+" "
            else:
                printobj = ";" + name+"."+recurname+"."+key+" "
            fileWriteOp = str(now)+printobj+"Entry\n"
            file1.write(fileWriteOp)
            fl = 1
            for j in currobj:
                if(j == "Inputs"):
                    fl = 0
            if(fl == 0):
                # only if its a executable function
                inputs = currobj['Inputs']
                funname = currobj['Function']
                time = inputs['ExecutionTime']
                fileWriteOp = ""
                # write the output to fsile
                fileWriteOp = str(now)+printobj+"Executing " + \
                    funname+" ("+inputs['FunctionInput']+", "+time+")\n"
                file1.write(fileWriteOp)
                now = now + timedelta(seconds=int(time))
                #now += timedelta(seconds=int(time))
                fileWriteOp = ""
                fileWriteOp = str(now)+printobj+"Exit\n"
                file1.write(fileWriteOp)
            else:
                seqfunction(currobj['Activities'], name, file1, key)
                #file1.write("In process \n")
                # write the output to file
                fileWriteOp = ""
                fileWriteOp = str(now)+printobj+"Exit\n"
                file1.write(fileWriteOp)
    file1 = open("klaout.txt", "w")
    mainservice = service['M1A_Workflow']
    name = "M1A_Workflow"
    fileobj = str(now)+";"+name+" Entry\n"
    file1.write(fileobj)
    for key in mainservice:
        if mainservice[key] == 'Sequential':
            stri = "None"
            seqfunction(mainservice['Activities'], name, file1, stri)
            fileWriteOp = ""
            fileWriteOp = str(now)+";"+name+" Exit\n"
            file1.write(fileWriteOp)
        # else:
            # concurrentfunction(mainservice['Activities'])
            # print(service['M1SampleSubTask1']['Task'])
            # print(service['M1A_Workflow']['M1SampleSubFlow']['M1SampleSubTask1'])