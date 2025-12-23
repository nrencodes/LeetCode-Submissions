class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 or not hand:
            return False
        
        h = Counter(hand)

        minH = list(h.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in h:
                    return False
                h[i] -= 1 
                if h[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True
            
            


            