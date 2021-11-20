import json



def oras():
    f=open("F:/junction/junction-falcon/backend/flask/db/oras-db.json")
    data=json.load(f)
    h=data["houses"]
    cons=[]
    flowt=[]
    timest=[]
    
    print(len(h[0]["apartments"]))
    
    for i in range(20):
        keys=list(h[0]["apartments"][0].keys())
        x=1
        print(len(keys))

        while x<6:
            for y in h[0]["apartments"][i][keys[x]]["measurements"]:
                cons.append(h[0]["apartments"][i][keys[x]]["measurements"][0]["Consumption"])#
                flowt.append(h[0]["apartments"][i][keys[x]]["measurements"][0]["FlowTime"])
                timest.append(h[0]["apartments"][i][keys[x]]["measurements"][0]["TimeStamp"])
            x=x+1
        
    # print(h[0]["apartments"][0]["Kitchen_optima_faucet"]["measurements"][0].keys())#
    print (len(cons),len(flowt),len(timest))
    
    f.close()




def elisa():
    pass


oras()
