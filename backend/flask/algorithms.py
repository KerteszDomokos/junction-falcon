import json
import numpy as np
import matplotlib.pyplot as plt
from os import walk
# from shapely.geometry import Polygon

import folium
def col(c):
    if c==0:
        return "color:red;"
    elif c==1:
        return "color:yellow;"
    else:
        return "color:green;"    
def elisa():
    
    m = folium.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')
    for x in range(1,4):
        f=open("F:/junction/4G/4G_tahtiluokka_"+str(x)+".json")
        data=json.load(f)    
        f.close()

        st0 = {'fillColor': '#bf0b0b', 'color': '#bf0b0b'}
        st1 = {'fillColor': '#ff7b00', 'color': '#ff7b00'}
        st2 = {'fillColor': '#228B22', 'color': '#228B22'}
        for i in range(len(data["features"])):
            if x==1: folium.GeoJson(data["features"][i]["geometry"],style_function=lambda x:st0,).add_to(m)
            if x==2: folium.GeoJson(data["features"][i]["geometry"],style_function=lambda x:st1,).add_to(m)
            if x==3: folium.GeoJson(data["features"][i]["geometry"],style_function=lambda x:st2,).add_to(m)

        path='F:/junction/vis/map.html'
    m.save(path)

    
elisa()


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


