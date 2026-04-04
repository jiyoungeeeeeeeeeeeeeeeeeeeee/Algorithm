import sys

n = int(sys.stdin.readline())
dic = {}
blst = []

for i in range(n-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())

    if a not in dic:
        dic[a] = []
    dic[a].append(b)

    if b not in dic:
        dic[b] = []
    dic[b].append(a)

            
# 각 노드의 부모를 저장할 리스트
# parent[x] = x번 노드의 부모 번호
parent = [0] * (n + 1)

# 방문했는지 확인하는 리스트
# visited[x] = x번 노드를 이미 방문했는가
visited = [False] * (n + 1)

# DFS에 사용할 스택
# 처음에는 루트 노드 1번만 넣어둠
stack = [1]

# 1번 노드는 시작하자마자 방문 처리
visited[1] = True

# 스택이 빌 때까지 반복
while stack:
    # 스택 맨 뒤에서 하나 꺼내서 현재 노드로 사용
    now = stack.pop()

    # 현재 노드와 연결된 모든 노드 확인
    for next_node in dic[now]:

        # 아직 방문하지 않은 노드라면
        if visited[next_node] == False:

            # 방문 처리
            visited[next_node] = True

            # next_node를 now에서 처음 발견했으므로
            # next_node의 부모는 now
            parent[next_node] = now

            # 나중에 next_node와 연결된 노드들도 확인해야 하므로
            # 스택에 넣기
            stack.append(next_node)

# 2번 노드부터 n번 노드까지 부모 출력
for i in range(2, n + 1):
    print(parent[i])