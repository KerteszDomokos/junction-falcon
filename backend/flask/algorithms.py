import json
import numpy as np
import matplotlib.pyplot as plt


def oras():
    f=open("F:/junction/junction-falcon/backend/flask/db/oras-db.json")
    data=json.load(f)    
    f.close()
    h=data["houses"]
    cons=[]
    flowt=[]
    timest=[]
    temps=[]
    pcons=[]
        
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
                temps.append(h[0]["apartments"][i][keys[x]]["measurements"][0]["Temp"])
                pcons.append(h[0]["apartments"][i][keys[x]]["measurements"][0]["Power_Consumption"])
            x=x+1
        
        
    figname="cons-flowt"
    # print(h[0]["apartments"][0]["Kitchen_optima_faucet"]["measurements"][0].keys())#
    print (len(cons),len(flowt),len(timest))
    fig, ax = plt.subplots()

        # Using set_dashes() to modify dashing of an existing line
    line1, = ax.plot(cons, flowt, label='figname')
    ax.legend()
    plt.show()
    plt.savefig("F:/junction/junction-falcon/backend/flask/vis/"+figname+".png")



def elisa():
    pass


oras()
