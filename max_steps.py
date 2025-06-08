MOD = 10**9 + 7

def max_operations(n):
    """
    Finds the maximum number of operations to reduce a number to 1 using divisors.
    This optimized version iterates through numbers and updates their multiples.
    The time complexity is approximately O(n log n).

    Args:
    n: The positive integer to be reduced to 1.

    Returns:
    The maximum number of operations (mod 10^9 + 7).
    """
    if n == 1:
        return 0

    # dp[x] will store the maximum number of operations to reduce x to 1.
    # Initialize dp[x] = 1 for x > 1, representing the operation x -> 1 (dividing by x itself).
    # dp[1] = 0 as 1 is already reduced.
    dp = [1] * (n + 1)
    dp[1] = 0 # Base case: 0 operations to reduce 1 to 1.

    # Iterate from i = 1 up to n.
    # For each number i, we consider it as a divisor for its multiples.
    # This is more efficient than iterating up to n and finding divisors for each number.
    for i in range(1, n + 1):
        # If dp[i] is already 0 and i is not 1, it means i is unreachable or an issue,
        # however, our initialization dp[i]=1 (for i > 1) and dp[1]=0 handles this.
        # We are looking for the number of operations to reduce i to 1, which is dp[i].

        # Now, iterate through multiples of i: 2*i, 3*i, ... up to n.
        # Let k be a multiple of i (e.g., k = i * j).
        # If we are at number k, and we divide k by j (where j = k/i), we get i.
        # So, the number of operations to reduce k to 1 could be:
        # (operations to reduce i to 1) + 1 (for the step k -> i).
        # This means dp[k] can be updated with dp[i] + 1.

        j = 2
        current_multiple = i * j
        while current_multiple <= n:
            # dp[i] stores the max operations to reduce i to 1.
            # To reduce current_multiple to 1, we can first reduce it to i (1 op),
            # then reduce i to 1 (dp[i] ops).
            dp[current_multiple] = max(dp[current_multiple], dp[i] + 1)
            j += 1
            current_multiple = i * j

    # Return the result for n, ensuring it's modulo MOD.
    return dp[n] % MOD

# Test cases
assert max_operations(1) == 0, "Test Case 1 Failed: n=1"
assert max_operations(2) == 1, "Test Case 2 Failed: n=2 (2->1)"
assert max_operations(3) == 1, "Test Case 3 Failed: n=3 (3->1)"
assert max_operations(4) == 2, "Test Case 4 Failed: n=4 (4->2->1)"
assert max_operations(5) == 1, "Test Case 5 Failed: n=5 (5->1)"
assert max_operations(6) == 2, "Test Case 6 Failed: n=6 (6->3->1 or 6->2->1)"
assert max_operations(7) == 1, "Test Case 7 Failed: n=7 (7->1)"
assert max_operations(10) == 2, "Test Case 8 Failed: n=10 (10->5->1 or 10->2->1)"
assert max_operations(12) == 3, "Test Case 9 Failed: n=12 (12->6->3->1 or 12->6->2->1 or 12->4->2->1)"
# For larger N, the original problem implies we need this to be efficient.
# Example: If n=2, dp[2] = max(dp[2], dp[1]+1) = max(1, 0+1) = 1.
# Example: If n=4
# i=1: dp[2]=max(dp[2],dp[1]+1)=1, dp[3]=max(dp[3],dp[1]+1)=1, dp[4]=max(dp[4],dp[1]+1)=1
# i=2: dp[4]=max(dp[4],dp[2]+1)=max(1,1+1)=2
# i=3: (no multiples <=4 other than 3 itself)
# i=4: (no multiples <=4 other than 4 itself)
# So, dp[4] = 2.

print("All basic test cases passed!")

# Call for user-requested test case n=5521
print(f"Result for n=5521: {max_operations(5521)}")

# Read the input number.
n = int(input())

# Calculate the maximum number of operations.
max_ops = max_operations(n)

# Print the result.
print(max_ops)
