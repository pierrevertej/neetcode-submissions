class Solution(object):
    def generateParenthesis(self, n):
        map = {'(' : [1,0]}
        for i in range(1, n * 2):
            newmap = {}
            for branch in map.keys():
                count = map.get(branch)
                if count[0] < n:
                    newmap.update({branch + '(': [count[0]+1, count[1]]})
                if count[0] > count[1]:
                    newmap.update({branch + ')': [count[0], count[1]+1]})
            map = newmap
        return list(map)