class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        answer = [(count, num) for num, count in counts.items()]
        heapq.heapify(answer)

        while len(answer) > k:
            heapq.heappop(answer)

        return [num for count, num in answer]
        
