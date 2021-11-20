import json
import numpy as np
import matplotlib.pyplot as plt
from os import walk
# from shapely.geometry import Polygon

import folium



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



def elisa():
    f=open("F:/junction/junction-falcon/4G/4G_tahtiluokka_1.json")
    data=json.load(f)    
    f.close()
    
    pol=[]
    for i in range(len(data["features"])):
        pol.append(data["features"][i]["geometry"]["coordinates"][0])
    
    
    print(len(pol))
    
    xl=[]
    yl=[]
    for i in range(len(data["features"][0]["geometry"]["coordinates"][0])):
        xl.append(data["features"][0]["geometry"]["coordinates"][0][i][0])
        yl.append(data["features"][0]["geometry"]["coordinates"][0][i][1])
    d=data["features"][0]["geometry"]
    polygon = zip(xl, yl)

    m = folium.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')
    
    for i in range(len(data["features"])):
        folium.GeoJson(data["features"][i]["geometry"]).add_to(m)
    
    
    # folium.LatLngPopup().add_to(m)
    # folium.GeoJson(data).add_to(map)
    path='F:/junction/junction-falcon/backend/flask/vis/map.html'
    m.save(path)
    
    # path="F:/junction/junction-falcon/backend/flask/vis/"
    # filenames = next(walk(path), (None, None, []))[2]  # [] if no file
    # nums=[]
    # for i in range(len(filenames)):
    #     try:
    #         nums.append(int(filenames[i].replace(figname,"").replace(".png","")))
    #     except:
    #         pass
    # nums.sort()
    # id=len(nums)

    # print (filenames)
    # plt.savefig(path+figname+str(id)+".png")
    
elisa()
#elisa()
#poligon lista(id) -> join és szín
