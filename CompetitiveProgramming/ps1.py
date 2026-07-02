def choclate_distribution(B,C,N):
    total_choco = B*C
    num_choco_each = total_choco // N
    num_choco_child = total_choco % N

    return num_choco_each,num_choco_child




T = int(input())
for i in range(T):
    B,C,N = map(int,input().split())
    X,Y = choclate_distribution(B,C,N)

    print(f"{X} {Y}")