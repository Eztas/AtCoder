N, Q = map(int,input().split())

server = ""
pc = ["" for _ in range(N)]

for q in range(Q):
    query = input().split()
    if query[0] == "1":
        pc[int(query[1])-1] = server

    elif query[0] == "2":
        pc[int(query[1]) - 1] += query[2]
        
    elif query[0] == "3":
        server = pc[int(query[1])-1]

print(server)
