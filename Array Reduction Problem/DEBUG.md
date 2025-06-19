# Array Challenge Debugging Steps

## Step-by-Step Debugging Process

### 1. Test with the Given Example
Start by testing your function with the provided test case:
```python
result = ArrayChallenge([5, 7, 16, 1, 2])
print(f"Result: {result}")  # Should output 7
```

### 2. Add Debug Print Statements
Insert print statements to track the array at each iteration:
```python
def ArrayChallenge(arr):
    print(f"Starting array: {arr}")
    iteration = 1
    
    while len(arr) > 1:
        print(f"Iteration {iteration}: Current array: {arr}")
        new_arr = []
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            new_arr.append(diff)
        arr = new_arr
        print(f"After iteration {iteration}: {arr}")
        iteration += 1
    
    print(f"Final result: {arr[0]}")
    return arr[0]
```

### 3. Manual Calculation Check
For `[5, 7, 16, 1, 2]`, manually verify each step:
- **Step 1:** `[5, 7, 16, 1, 2]` → `[2, 9, 15, 1]`
- **Step 2:** `[2, 9, 15, 1]` → `[7, 6, 14]`
- **Step 3:** `[7, 6, 14]` → `[1, 8]`
- **Step 4:** `[1, 8]` → `[7]`
- **Result:** `7`

### 4. Common Issues to Check

#### Issue 1: Index Out of Range
**Problem:** Accessing `arr[i+1]` when `i` is the last index
**Solution:** Ensure loop range is `range(len(arr) - 1)`

#### Issue 2: Infinite Loop
**Problem:** While loop never terminates
**Check:** Verify that `len(arr)` decreases by 1 each iteration
**Debug:** Add `print(f"Array length: {len(arr)}")` inside the loop

#### Issue 3: Wrong Differences
**Problem:** Not using absolute values or incorrect calculation
**Check:** Ensure you're using `abs(arr[i] - arr[i + 1])`

#### Issue 4: Empty Array Handling
**Problem:** Function fails with empty or single-element arrays
**Solution:** Add input validation:
```python
if len(arr) <= 1:
    return arr[0] if arr else 0
```

### 5. Test Edge Cases
```python
# Test various inputs
test_cases = [
    [1],           # Single element
    [1, 2],        # Two elements
    [5, 5, 5],     # All same elements
    [1, 2, 3, 4],  # Sequential numbers
]

for test in test_cases:
    print(f"Input: {test}, Output: {ArrayChallenge(test)}")
```

### 6. Performance Check
For large arrays, ensure the algorithm completes in reasonable time:
```python
import time
start_time = time.time()
result = ArrayChallenge(your_array)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")
```

### 7. Clean Up Debug Code
Once debugging is complete, remove all print statements for the final submission.