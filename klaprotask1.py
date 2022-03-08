import yaml
from datetime import datetime, timedelta
now = datetime.now()
with open(r'C:\Users\ramal\OneDrive\Desktop\kla\test.yaml') as file:
    service = yaml.safe_load(file)

    def seqfunction(activity, name, now):
        file1 = open("klaout.txt", "w")
        for key in activity:
            currobj = activity[key]
            printobj = "; " + name+"."+key+" "
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
                # write the output to file
                fileWriteOp = str(now)+printobj+"Executing" + \
                    funname+"("+inputs['FunctionInput']+","+time+")\n"
                file1.write(fileWriteOp)
                now = now + timedelta(seconds=int(time))
                now += timedelta(seconds=int(time))
            else:
                #file1.write("In process \n")
                # write the output to file
                fileWriteOp = ""
                fileWriteOp = str(now)+printobj+"Exit\n"
                file1.write(fileWriteOp)
    mainservice = service['M1SampleWorkFlow']
    name = "M1SampleWorkFlow"
    for key in mainservice:
        if mainservice[key] == 'Sequential':
            seqfunction(mainservice['Activities'], name, now)
        # else:
            # concurrentfunction(mainservice['Activities'])
            # print(service['M1SampleSubTask1']['Task'])
            # print(service['M1SampleWorkFlow']['M1SampleSubFlow']['M1SampleSubTask1'])