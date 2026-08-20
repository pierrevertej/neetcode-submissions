class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        side=int(sum(matchsticks)/4)
        cases=[{side:4}]
        nextcases=[]
        for i in range(len(matchsticks)):
            num=matchsticks[i]
            for case in cases:
                for key in case:
                    if key>=num:
                        newcase=case.copy()
                        if case[key]==1:
                            newcase.pop(key)
                        else:
                            newcase[key]=newcase[key]-1
                        newval=key-num
                        if newval in case:
                            newcase[newval]=newcase[newval]+1
                        else:
                            newcase[newval]=1
                        nextcases.append(newcase)
            cases=nextcases
            nextcases=[]
        return len(cases)>0
                        

                        


