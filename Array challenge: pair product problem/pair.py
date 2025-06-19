def ArrayChallenge(arr):
    """
    Check if any two numbers in the array can be multiplied 
    to get a result greater than double the sum of all elements.
    
    Args:
        arr: List of integers
    
    Returns:
        String: "true" if condition is met, "false" otherwise
    """
    
    # Step 1: Calculate the sum of all elements in the array
    total_sum = sum(arr)
    
    # Step 2: Double the sum to get our comparison threshold
    double_sum = 2 * total_sum
    
    # Step 3: Check all possible products of two different elements
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # Start j from i+1 to avoid same element
            product = arr[i] * arr[j]
            
            # Step 4: If any product exceeds double the sum, return "true"
            if product > double_sum:
                return "true"
    
    # Step 5: If no product exceeds double the sum, return "false"
    return "false"


# Test the function with provided examples
if __name__ == "__main__":
    # Test case 1
    test1 = [2, 2, 2, 2, 4, 1]
    result1 = ArrayChallenge(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print(f"Expected: false")
    print()
    
    # Test case 2
    test2 = [1, 1, 2, 10, 3, 1, 12]
    result2 = ArrayChallenge(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print(f"Expected: true")
    print()
    
    # Test case 3 (from problem description)
    test3 = [2, 5, 6, -6, 16, 2, 3, 6, 5, 3]
    result3 = ArrayChallenge(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print(f"Expected: true")

# Keep this function call here (as required by the template)
print(ArrayChallenge(input()))