class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = []
        n = len(costs) // 2
        for costA, costB in costs:
            differences.append((costA - costB, costA, costB))
        res = 0
        differences = sorted(differences, key=lambda x: x[0])
        print(differences)
        for i in range(len(costs)):
            if i < n: 
                res += differences[i][1]
            else:
                res += differences[i][2]

        return res