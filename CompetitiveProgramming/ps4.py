def valid_pairs(dp, K):
    pairs = 0
    used = [False] * len(dp)  

    for i in range(len(dp)):
        if used[i]:
            continue
        for j in range(i+1, len(dp)):
            if not used[j] and dp[i] + dp[j] == K:
                pairs += 1
                used[i] = True
                used[j] = True
                break  

    return pairs


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    danger_person = list(map(int, input().split()))
    danger_person = danger_person[:N]
    
    num_valid_pairs = valid_pairs(danger_person, K)
    print(num_valid_pairs)
