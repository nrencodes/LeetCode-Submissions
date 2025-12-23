class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 or not hand:
            return False
        
        h = Counter(hand)
        keys = sorted(h.keys()) 

        for x in keys:
            # How many lists are started from the current key
            need = h[x]
            if need == 0:
                continue

            # iterate over the current number and two consecutive numbers in the frequency chart
            for v in range(x, x + groupSize):
                # if the next numbers don't have as many occurrences needed to create the "need" number
                # of sets, it means there will be an incomplete set so immediately return False. 
                if h[v] < need:
                    return False
                # Otherwise, decrement the needed amount of the number and progress to the next key
                h[v] -= need

        return True
            
            


            