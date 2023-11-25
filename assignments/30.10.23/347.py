class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict={}
        L =[]
        for i in nums:
            if i in Dict:
                Dict[i]+=1
            else:
                Dict[i]=1
        idx=sorted(Dict.values(),reverse=True)[k-1]
        for i in Dict:
            if Dict[i]<idx:
                continue
            else:
                L.append(i)
        return L