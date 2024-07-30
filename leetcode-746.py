class solution:
    def climbstairs(self,cost):
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        print(cost)
        return min(cost[-1],cost[-2])

cost=[1,100,1,1,1,100,1,1,100,1]
sol=solution()
a=sol.climbstairs(cost)
print(a)
