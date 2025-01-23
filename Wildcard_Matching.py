class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Approach:
        # Use dynamic programming to determine if the string 's' matches the pattern 'p'.
        # We define a 2D DP table dp[i][j] where:
        # - dp[i][j] is True if the first i characters of 's' match the first j characters of 'p'.
        # - '?' matches any single character.
        # - '*' matches any sequence of characters (including an empty sequence).

        # Time Complexity: O(m * n) where m is the length of 's' and n is the length of 'p'.
        # Space Complexity: O(m * n) due to the DP table.
        # Did this code successfully run on Leetcode: Yes
        # Any problem you faced while coding this: No

        # Length of the input string and the pattern
        m, n = len(s), len(p)

        # Initialize a DP table with dimensions (m+1) x (n+1) and set all values to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches with empty pattern
        dp[0][0] = True

        # Handle the cases where the pattern consists of only '*' characters
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    # If characters match or '?' matches any single character
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can either match no characters (dp[i][j-1]) or match one/more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        # Return the value in the last cell of the DP table
        return dp[m][n]
