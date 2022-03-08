import yaml
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# with open(r'C:\Users\ramal\OneDrive\Desktop\kla\test.yaml') as file:
#     items = yaml.load(file, Loader=yaml.FullLoader)
#     print(items)
with open(r'C:\Users\ramal\OneDrive\Desktop\kla\test.yaml') as file:
    service = yaml.safe_load(file)
    # print(service['M1SampleWorkFlow']['Type'])
    # print(service['M1SampleWorkFlow']['Execution'])
    # print(service['M1SampleWorkFlow']['Activities']
    #       ['M1SampleSubFlow']['Activities']['M1SampleSubTask1'])

    def seqfunction(activity, name):
        for key in activity:
            currobj = activity[key]
            print(current_time+";", name, ".", key, " ", "Entry")
            if(currobj['Inputs']):
                inputs = currobj['Inputs']
                funname = currobj['Function']
                time = inputs['ExecutionTime']
                print(inputs['FunctionInput'], ",", time)
    # def concurrentfunction(activity):
       # a=''
    mainservice = service['M1SampleWorkFlow']
    name = "M1SampleWorkFlow"
    for key in mainservice:
        #print(key, ":", service[key])
        if mainservice[key] == 'Sequential':
            seqfunction(mainservice['Activities'], name)
        # else:
            # concurrentfunction(mainservice['Activities'])
            # print(service['M1SampleSubTask1']['Task'])
            # print(service['M1SampleWorkFlow']['M1SampleSubFlow']['M1SampleSubTask1'])