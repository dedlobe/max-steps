MOD = 10**9 + 7

def max_operations(n):
    """
    Finds the maximum number of operations to reduce a number to 1 using divisors.

    Args:
    n: The positive integer to be reduced to 1.

    Returns:
    The maximum number of operations (mod 10^9 + 7).
    """
    if n == 1:
        return 0

    # Initialize the dp array to store the maximum number of operations for each number.
    dp = [0] * (n + 1)

    # Iterate through numbers from 2 to n.
    for i in range(2, n + 1):
        # Initialize max_ops to 1 (operation to divide by itself).
        max_ops = 1

        # Iterate through divisors of i up to square root of i.
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # Update max_ops with maximum of current value and dp[j] + 1.
                max_ops = max(max_ops, dp[j] + 1)

                # If i//j is different from j, update max_ops with dp[i//j] + 1.
                if i // j != j:
                    max_ops = max(max_ops, dp[i // j] + 1)

        # Store the maximum number of operations for the current number.
        dp[i] = max_ops

    # Return the maximum number of operations for n modulo 10^9 + 7.
    return dp[n] % MOD

# Read the input number.
n = int(input())

# Calculate the maximum number of operations.
max_ops = max_operations(n)

# Print the result.
print(max_ops)