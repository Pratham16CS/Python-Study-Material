def money_superman(money):
    prev1,prev2 = 0,0
    for i in money:
        curr_max = max(prev1,prev2+i)
        prev2 = prev1
        prev1 = curr_max

    return prev1


def max_money_superman(money,N):
    if len(money) == 1:
        return money[0]
    a = money_superman(money[1:])
    b = money_superman(money[:N-1])

    return max(a,b)

T = int(input())
for i in range(T):
    N = int(input())
    money = list(map(int,input().split()))
    money = money[:N]
    max_money = max_money_superman(money,N)
    print(max_money)