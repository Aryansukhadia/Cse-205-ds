class Solution(object):
    def reverseString(self, s):
        end = len(s) - 1
        def recursiveReverse(s, index):
            
            if index < len(s)/2:
                s[index], s[end-index] = s[end-index],s[index]
                index =  index + 1
                recursiveReverse(s,index)
            else:
                return
        
        recursiveReverse(s,0)
