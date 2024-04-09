class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        # for i in range(tickets[k]):
        while tickets[k] > 0:
            v = 0
            # for j in tickets:
            for j in range(len(tickets)):
                # if j > 0:
                if tickets[j] != 0:
                    tickets[j] -= 1
                    # v += 1
                    time += 1
                    if tickets[k] == 0:
                        return time
        return time

