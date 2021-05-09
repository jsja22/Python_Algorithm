from heapq import heappush,heappop
import sys

INF = int(1e9)
graph =[[]]
a =[]
def update_road(n,s_node,e_node,roads,trap,n_node):    
    global graph
    global a
    update_n_node = n_node
    print("udate_n_node:",n_node)
    if trap==True:
        print("***********")
        for road in roads:
            #print("roads:",roads)
            print("road[0]:",road[0])
            print("road[1]:",road[1])

            if road[0] == update_n_node or road[1] == update_n_node:
                print("update_n_node:", update_n_node)
                a.append(road[0])
                a.append(road[1])
                road[0] = a[1]
                road[1] = a[0]
                a=[]
                print("road:",road)
    graph = [[]for i in range(n+1)]
    
    for road in roads:
        s_node, e_node, cost = road[0], road[1], road[2]
        graph[s_node].append([e_node,cost])

    print(graph)
def preprocess(n, roads):
    global graph
    #각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
    graph = [[]for i in range(n+1)]
    
    for road in roads:
        s_node, e_node, cost = road[0], road[1], road[2]
        graph[s_node].append([e_node,cost])

    print(graph)

def dijkstra(n,s_node,e_node,roads,traps):
    global graph
    table = [INF for i in range(n+1)]
    table[s_node] = 0
    print(table)
    pq = [[0,s_node]]

    while pq:
        dist, now = heappop(pq)

        
        for item in graph[now]:
            trap = False
            print("graph[now] :",graph[now])
            n_node, cost = item[0], item[1]
            print("n_node:", n_node)
            cost +=dist
            print("cost:", cost)
            
            if n_node in traps:
                trap = True
                update_road(n,s_node,e_node,roads,trap,n_node)
            if cost< int(1e9):
                if n_node != s_node: 
                    table[n_node] = cost
                    heappush(pq,[cost,n_node])
        print("pq: ",pq)
    print(table)
    return table[e_node]
n,start,end = 4,1,4
roads = [[1, 2, 1], [3, 2, 1],[2,4,1]]
traps = [2,3]
print(preprocess(n,roads))
print(dijkstra(n,start,end,roads,traps))

