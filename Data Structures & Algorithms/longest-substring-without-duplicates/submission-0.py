class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        sub=set()
        extra={}
        for i in range(len(s)):
            if s[i] in sub:
                if s[i] in extra:
                    extra[s[i]]=extra[s[i]]+1
                else:
                    extra[s[i]]=1
                first=s[i-res]
                if first in extra:
                    if extra[first]==1:
                        extra.pop(first)
                    else:
                        extra[first]=extra[first]-1
                else:
                    sub.remove(first)
            elif extra:
                sub.add(s[i])
                first=s[i-res]
                if first in extra:
                    if extra[first]==1:
                        extra.pop(first)
                    else:
                        extra[first]=extra[first]-1
                else:
                    sub.remove(first)
            else:
                sub.add(s[i])
                res+=1
        return res