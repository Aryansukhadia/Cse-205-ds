class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for i in range(len(score)):
            heapq.heappush(heap, [-score[i], i])
        answer = [0] * len(score)
        rank = 1
        while heap:
            s, index = heapq.heappop(heap)
            if rank == 1:
                answer[index] = "Gold Medal"
            elif rank == 2:
                answer[index] = "Silver Medal"
            elif rank == 3:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank)
            rank += 1
        return answer