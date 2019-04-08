"""
Created on Fri Mar 23 06:27:39 2018
PRIMS ALGORITHM
@author: Arya Saumitra
"""

import queue as q
import math
m=math.inf
Q=q.PriorityQueue()
                        # remove the duplicates from created adjacency list
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
       
    return output
                            #create a adjacent list of given vertices 
def CreateAdj(name,edges):
        
        adj=[]
        for eachedge in edges:
            if name==eachedge[1]:
                adj.append(eachedge[2])
            elif name==eachedge[2]:
                adj.append(eachedge[1])
           
        adj=remove_duplicates(adj)
        return adj
                            
                            #return the weight of each node passed
def ret_weight(node,vertice):
    #print(vertice)
    for v in vertice:
        #print(v)
        if node==v[1]:
            return v[0]
        
        
                            #set the required key for a given vertice
def set_key(target,value,verticelist):
    for eachv in verticelist:
        if target==eachv[1]:
            #print(eachv)
            #print(target)
            eachv[0]=value
            break
            #print(eachv)
                            #set the predeccesor for a given vertice
def set_pred(target,value,verticelist):
    for eachv in verticelist:
        if target==eachv[1]:
            #print(eachv)
            #print(target)
            eachv[2]=value
            #print(eachv)
            break
                            #return the weight between two given nodes
def weight(var1,var2,edgelist):
    for er in edgelist:
        if er[1]==var1 and er[2]==var2:
            return er[0]
        elif er[2]==var1 and er[1]==var2:
            return er[0]
                        #return vertice list
def ret_ver(ti):
    out=[]
    for eachnode in ti:
        out.append(eachnode[1])
    return out
                       #prims method with parameters graph(dictionary) adjacency list(dictionary) and source node
def prims(graph,adj,sr):

    for each in graph['vertices']:
        if sr==each[1]:
            each[0]=0
            break
    for ver in graph['vertices']:
        Q.put(ver)
    while not Q.empty():
        
        ut=Q.get()
        u=ut[1]
        if not Q.empty():
            for ea in adj[u]:
                d=Q.queue
                t=ret_ver(d)
                val1=weight(u,ea,graph['edges'])
                val2=ret_weight(ea,graph['vertices'])
                if(ea in t) and (val1<val2):
                    set_key(ea,val1,graph['vertices'])
                    set_pred(ea,u,graph['vertices'])
        
#complete the else part of the code asshole



a1=[]
v1=[[m,'a',None], [m,'b',None], [m,'c',None], [m,'d',None], [m,'e',None], [m,'f',None], [m,'g',None], [m,'h',None], [m,'i',None]]
e1=[[4, 'a', 'b'], [11, 'b', 'h'], [8, 'b', 'c'], [7, 'c', 'd'], [14, 'd', 'f'], [9, 'd', 'e'], [10, 'e', 'f'], [2, 'f', 'g'],[6, 'g', 'i'], [1, 'g', 'h'], [7, 'i', 'h'], [8, 'h', 'a']]


graph={'vertices':v1,'edges':e1}
adjacency={}

#create a adjacency dictionary for each given node
for eachvertice in graph['vertices']:
    dict1={eachvertice[1]:CreateAdj(eachvertice[1],graph['edges'])}
    adjacency.update(dict1)


prims(graph,adjacency,'h') #passing the graph

print(graph['vertices'])
        
       
    