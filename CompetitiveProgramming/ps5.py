def min_energy_crystal(crystal,M):
    iter_away = set([0])
    for energy in crystal:
        iter_away.add((M - energy) % M)

    min_energy = float('inf')
    for i in iter_away:
        total = sum((e + i) % M for e in crystal)
        if total < min_energy:
            min_energy = total

    return min_energy




T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    crystal_energy = list(map(int,input().split()))
    crystal_energy = crystal_energy[:N]
    min_energy = min_energy_crystal(crystal_energy,M)
    print(min_energy)