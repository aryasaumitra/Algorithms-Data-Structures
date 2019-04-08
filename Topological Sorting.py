# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:21:52 2018

@author: Arya Saumitra
"""
import math


#Function to print the graph
def printGraph(a):
    for i in a:
        for j in i:
            print(j,end=" ")
        print()

#Fuction to Print Sorted Graph        
def printSortedGraph(sortedlist):
    for eachele in sortedlist:
        print(str(eachele)+"-->",end=" ")
    print()
        
#Input of the Graph:
indegree={}
numberOfVertices=int(input("Enter Number of Vertices:"))
graph=[[0 for i in range(numberOfVertices)] for j in range(numberOfVertices)]


for each in range(numberOfVertices):
    indegree[each+1]=0
    
n=math.inf
for i in range(numberOfVertices):
    print("Enter Adjacency of {} and press '0' to terminate:".format(i+1))
    while n!=0:
        n=int(input("Enter the adjacent node:"))
        if n!=0:
            graph[i][n-1]=1
            indegree[n]+=1
    n=math.inf
    
#Function For Topological Sorting
def topologicalSorting(g,indeg,n):
    l=[]
    count=n+1
    while count>0:
        for eachkey in indeg.keys():
            #print("EachKey:"+str(eachkey))
            if indeg[eachkey]==0 and indeg[eachkey]!=-1:
                #print("Indegree[eachkey]:"+str(indeg[eachkey]))
                for j in range(n):
                    if g[eachkey-1][j]==1:
                        indeg[j+1]-=1
                        g[eachkey-1][j]=0
                l.append(eachkey)
                indeg[eachkey]=-1
            count-=1
    printSortedGraph(l)
    
    
#Calling The Functions
printGraph(graph)
print(indegree)
topologicalSorting(graph,indegree,numberOfVertices)