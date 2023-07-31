if __name__ == "__main__":
    input1 = list(map(int,input().split()))
    loopedList = []
    calculatedLoopedList = []
    calculatedSumLoopedList = []
    for i in range(1,input1[0]*2,2):
        listInputs = list(map(int,input().split()))
        loopedList.append(listInputs[(i)])
    for i in range(len(loopedList)):
        calculatedLoopedList.append((loopedList[i])**2)


    # print(loopedList)
    # print(calculatedLoopedList)
    # print((sum(calculatedLoopedList)))        
    print((sum(calculatedLoopedList))%input1[1])        

        
