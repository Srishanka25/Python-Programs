''''class Solution(object):
    def shortestToChar(self, s, c):
        l=[]
        for i in range(len(s)):
            if s[i]==c:
                l.append(i)
        l.sort()
        res=[]
        for j in range(len(s)):
            min_distance=float('inf')
            for pos in l:
                min_distance=min(min_distance, abs(j - pos))
            res.append(min_distance)
        return res'''
#2(leetcode problem)shortest distance to a character
res = [i for i in range(len(s)) if s[i]==c]
        return [abs(min(res,key = lambda x:abs(x-i))-i) for i in range(len(s))]