# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:33:31 2018

@author: bpou
"""
from matplotlib.pyplot import show
import networkx
BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLG = 'Heilongjiang'
NY = 'New York City'
CM = 'Chiangmai'
SG = 'Singapore'


air_route = {
    BJ : {SZ, GZ, WH, HLG, NY}, 
    GZ : {WH, BJ, CM, SG},
    SZ : {BJ, SG},
    WH : {BJ, GZ},
    HLG : {BJ},
    CM : {GZ},
    NY : {BJ}
}

air_route = networkx.Graph(air_route)

#networkx.draw(air_route, with_labels=True)


def search_destination(graph, start, destination):
    pathes = [[start]]
    visited = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        #print (path)
        frontier = path[-1]
        if frontier in visited: 
            continue
        # get new lines
        
        for city in graph[frontier]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: 
               # print (new_path)
                return new_path
        
        visited.add(frontier)
    return chosen_pathes

def draw_route(cities): return ' ✈️ -> '.join(cities)

print(draw_route(search_destination(air_route, SZ, CM)))