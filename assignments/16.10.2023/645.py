class Solution(object):
    def wordPattern(self, pattern, s):
        dic = {}
        s = s.split()
        k = pattern
        if len(s)!=len(k):
            return False
        if (len(set(s)))!=(len(set(k))):
            return False
        for i in range(len(k)):
            if k[i] not in dic:
                dic[k[i]]=s[i]
            elif dic[k[i]]==s[i]:
                continue
            else:
                return False
        return True