# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:23:56 2018

@author: Arya Saumitra
"""
import math
m=math.inf                  # m=infinity

class PQueue(object):
    
    def __init__(self):
        self.pqueue=[]
   
        
    def extract_min(self):
        data=self.pqueue[0]
        self.pqueue.remove(data)
        return data
    def isEmpty(self):
        return self.pqueue==[]
    
    def sort(self):
        n=len(self.pqueue)
        for i in range(n):
            for j in range(i+1,n):
                if self.pqueue[i][0]>self.pqueue[j][0]:
                    self.pqueue[i],self.pqueue[j]=self.pqueue[j],self.pqueue[i]
        
    def put(self,value):
        self.pqueue.append(value)
        self.sort()
    def disp(self):
        print(self.pqueue)
        
    def update(self,source,adjacent,edgelist):
        for each in self.pqueue:
            if each[1]==adjacent:
                if each[0]>source[0]+distance(source[1],adjacent,edgelist):
                    
                   # print(source[1],end=" ")
                   # print(adjacent,end=" ")
                   # print(distance(source[1],adjacent,edgelist))
                    each[0]=source[0]+distance(source[1],adjacent,edgelist)
                    #print(each[0])
                    each[2]=source[1]
        self.sort()
            
                            #create a adjacent list of given vertices 
def CreateAdj(name,edges):
        
        adj=[]
        for eachedge in edges:
            if name==eachedge[1]:
                adj.append(eachedge[2])
            #elif name==eachedge[2]:
             #   adj.append(eachedge[1])
           
        adj=remove_duplicates(adj)
        return adj

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
        elif value not in seen:
            output.append(value)
            seen.add(value)
    return output

                            #return the distance between two given nodes
def distance(var1,var2,edgelist):
    for er in edgelist:
        if er[1]==var1 and er[2]==var2:
            return er[0]
      
        
def set_dist(target,value,verticelist):
    for each in verticelist:
        if target==each[1]:
            each[0]=value
        
def dijkstra(graph,source,adj):
    set_dist(source,0,graph['vertices'])
    s=[]
    Q=PQueue()
    for ver in graph['vertices']:
        Q.put(ver)
        
    while not Q.isEmpty():
        
        ut=Q.extract_min()
        s.append(ut)
        #print(ut)
        for ea in adj[ut[1]]:
            Q.update(ut,ea,graph['edges'])
            
            
    for each in s:
        print("Distance of node:"+str(each[1])+" from Source:"+str(source)+" is :"+str(each[0])+" and Predeceesor is:"+str(each[2]))
    
    
v1=[[m,'s',None], [m,'t',None], [m,'y',None], [m,'x',None], [m,'z',None]]
e1=[[10, 's', 't'], [5, 's', 'y'], [2, 't', 'y'], [3, 'y', 't'], [1, 't', 'x'], [9, 'y', 'x'], [4, 'x', 'z'], [2, 'y', 'z'],[6, 'z', 'x'],[7,'z','']]



graph={'vertices':v1,'edges':e1}
adjacency={}

#create a adjacency dictionary for each given node
for eachvertice in graph['vertices']:
    dict1={eachvertice[1]:CreateAdj(eachvertice[1],graph['edges'])}
    adjacency.update(dict1)
    
    
sour=input("Enter Source Node:")
dijkstra(graph,sour,adjacency)