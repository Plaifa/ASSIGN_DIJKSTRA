import csv

def Dijkstra(file,start,end):
    with open(file+'.csv','r') as f:
        reader = csv.reader(f)
        graph = list(reader)
    dictName = {}

    for i in range (1,len(graph[0])):
        dictName[graph[0][i]] = i

    print('Graph is : \n\t\t',end='')
    for i in range(1, len(graph[0])):
        print(graph[0][i],end='\t')
    print()
    for i in range(1, len(graph[0])):
        print(graph[i][0],end='\t:\t')
        for j in range(1, len(graph[0])):
            print(graph[i][j], end='\t')
        print()
    print('Start at :',start)
    print('End at :',end)
    isStart=0
    isEnd=0
    for node in dictName.keys():
        if (node is start):
            isStart=1
            break
    for node in dictName.keys():
        if (node is end):
            isEnd=1
            break
    if isStart==0:
        print("CAN'T FIND START POINT")
        return 0
    if isEnd==0:
        print("CAN'T FIND End POINT")
        return 0
    current = start
    unreach = {node : None for node in dictName}
    path = {node: None for node in dictName}
    currentDistance=0
    unreach[current]=currentDistance
    reach = {}

    while True:
        print('========================\nCurrent node is ',current)
        for n ,addr in dictName.items():
            if n not in unreach:
                continue
            distance = int (graph[dictName[current]][addr])
            if (distance==0):       continue
            newDistance= currentDistance+distance
            if (path[current]==None):
                currentPath=current
            else:      currentPath=path[current]
            newPath = currentPath+","+n
            print('to ->',n)
            if unreach[n] is None or unreach[n] > newDistance:
                unreach[n] = newDistance
                path[n] =newPath
                print('Distance = ',currentDistance,'+',distance,'=',end=str(newDistance))
                print('\tPath => (',newPath,')\t\t --> New')
            else:
                print('Distance = ', unreach[n], end='\t')
                print('\tPath => (', path[n], ')\t\t --> old')
            if (n==end):
                reach[end]=unreach[end]
                print('\nFound ',end,'(end)')
                print(start , 'to' ,end,'\nDistance = ',end='')
                print(reach[end] ,'\npath = (',path[end],')')
                return 0
        reach[current] =currentDistance
        del unreach[current]
        candidate = [node for node in unreach.items() if node[1]]
        if not candidate:
            print('\n',end,'is unreachable')
            break
        current,currentDistance=sorted(candidate,key=lambda x: x[1])[0]
        print('\nUnvisited is : ',end=' ')
        for node in unreach.keys():
            print(node,end=' , ')
        print('\nNext node you can : ',sorted(candidate,key=lambda x: x[1]))
        print('Next node is ->',current)
    return 0


nameFile = input('input file name : ')
nodeStart=input('input start : ')
nodeEnd=input('input End : ')
Dijkstra(nameFile,nodeStart,nodeEnd)









