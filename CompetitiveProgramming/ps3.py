def visit_build_order(build,N):
    place = 0
    for i in build:
        if i != 0:
            build[place] = i
            place += 1
        
    while (place < len(build)):
        build[place] = 0
        place += 1

    return build


T = int(input())
for i in range(T):
    N = int(input())
    building_height = list(map(int,input().split()))
    building_height = building_height[:N]
    reorder_building_height = visit_build_order(building_height,N)
    print(*reorder_building_height)