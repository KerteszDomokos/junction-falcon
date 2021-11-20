import json
import numpy as np
import matplotlib.pyplot as plt
from os import walk
from datetime import datetime


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
        
        
    figname="cons-flowt-all"
    # print(h[0]["apartments"][0]["Kitchen_optima_faucet"]["measurements"][0].keys())#
    print (len(cons),len(flowt),len(timest))
    fig, ax = plt.subplots()
    
    cons, flowt = zip(*sorted(zip(cons, flowt)))        
    
    
        # Using set_dashes() to modify dashing of an existing line
    line1, = ax.plot(cons, flowt, label=figname)
    ax.legend()
    plt.show()

    path="F:/junction/junction-falcon/backend/flask/vis/"
    filenames = next(walk(path), (None, None, []))[2]  # [] if no file
    nums=[]
    for i in range(len(filenames)):
        try:
            nums.append(int(filenames[i].replace(figname,"").replace(".png","")))
        except:
            pass
    nums.sort()
    id=len(nums)

    print (filenames)
    plt.savefig(path+figname+str(id)+".png")



def elisa_create_pngs():
    f=open("db/4G_tahtiluokka_1.json")
    data=json.load(f)
    for i in range(0,len(data["features"])):
        print(coord)
        #coord.append(coord[0]) #repeat the first point to create a 'closed loop'

        #xs, ys = zip(*coord) #create lists of x and y values

        #plt.figure()
       ## plt.plot(xs,ys) 
        #plt.savefig("db/gen/4G_tahtiluokka_"+str(i)+".png")
        #f.close()
        print("Done : " + str(i))
    pass

elisa_create_pngs()

