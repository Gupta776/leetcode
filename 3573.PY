class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG_INF = float('-inf')

        # dp[t][state]
        # state: 0 = no position, 1 = long, 2 = short
        dp = [[NEG_INF, NEG_INF, NEG_INF] for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            for t in range(k, -1, -1):
                # open long
                dp[t][1] = max(dp[t][1], dp[t][0] - price)

                # open short
                dp[t][2] = max(dp[t][2], dp[t][0] + price)

                if t < k:
                    # close long
                    dp[t + 1][0] = max(dp[t + 1][0], dp[t][1] + price)

                    # close short
                    dp[t + 1][0] = max(dp[t + 1][0], dp[t][2] - price)

        return max(dp[t][0] for t in range(k + 1))
        
                
