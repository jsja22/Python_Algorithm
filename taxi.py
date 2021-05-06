from heapq import heappop, heappush

INF = int(1e9)
graph = [[]]

def preprocess(n, fares):
    global graph
    #각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[]for i in range(n+1)]

    for fare in fares:
        s_node, e_node, cost = fare[0], fare[1], fare[2]  #이전노드 다음노드 거리(비용)
        #s_node에서 e_node 로 가는 비용이 cost라는 의미
        graph[s_node].append([e_node,cost])
        graph[e_node].append([s_node,cost])
        
def dijkstra(s_node, e_node):
    global graph
    n = len(graph)
    table = [INF for i in range(n)] #최단거리 테이블을 모두 무한대로 초기화
    table[s_node] = 0
    pq = [[0,s_node]]
    #heapq.heappush(q, ([0,s_node]))

    while pq:
            dist, now = heappop(pq)

            if table[now] < dist: continue

            for item in graph[now]:
                n_node, cost = item[0], item[1]
                cost += dist
                if cost < table[n_node]:
                    table[n_node] = cost
                    heappush(pq, [cost, n_node])
        
    return table[e_node]

def solution(n,s,a,b,fares):
    preprocess(n, fares)
    cost = INF
    
    #COST는 최종 중에 가장 최소값
    #A,와B가 같이 합승한 거리 + A가 혼자 집까지 간거리 + B가 혼자 집까지 간거리
    for i in range(1, n+1):
        cost = min(cost, dijkstra(s,i) + dijkstra(i,a) + dijkstra(i,b))

    return cost

n ,s,a,b = 6,4,6,2 
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))