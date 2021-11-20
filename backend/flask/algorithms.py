import json



def oras():
    f=open("F:/junction/junction-falcon/backend/flask/db/oras-db.json")
    data=json.load(f)
    h=data["houses"]
    cons=[]
    flowt=[]
    time=[]
    
    print(h[0]["apartments"][0].keys())
    
    for i in range(20):
        keys=list(h[0]["apartments"][0].keys())
        print (keys)
        x=1
        print(h[i]["apartments"][0][keys[x]]["measurements"][0].keys())
        print(h[i]["apartments"][0][keys[x]].keys())
        print(i)
        while x<6:
            cons.append(h[i]["apartments"][0][keys[x]]["measurements"][0]["Consumption"])#
            flowt.append(h[i]["apartments"][0][keys[x]]["measurements"][0]["FlowTime"])
            time.append(h[i]["apartments"][0][keys[x]]["measurements"][0]["TimeStamp"])
            x=x+1
        
    # print(h[0]["apartments"][0]["Kitchen_optima_faucet"]["measurements"][0].keys())#
    print (len(cons))
    
    f.close()




def elisa():
    pass


oras()
