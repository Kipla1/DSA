# Array Challenge Instructions

## Problem Statement

Have the function `ArrayChallenge(arr)` take the array of numbers stored in `arr` and return the string **true** if any two numbers can be multiplied so that the answer is **greater than double the sum of all the elements** in the array. If not, return the string **false**.

## Example Explanation

For example: if `arr` is [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] then the sum of all these elements is 42 and doubling it is 84.

There are two elements in the array, 16 × 6 = 96 and 96 is greater than 84, so your program should return the string **true**.

## Test Cases

### Example 1
- **Input:** [2, 2, 2, 2, 4, 1]
- **Output:** false

### Example 2  
- **Input:** [1, 1, 2, 10, 3, 1, 12]
- **Output:** true

## Requirements

- Function name: `ArrayChallenge(arr)`
- Return type: String ("true" or "false")
- Must check all possible pairs of different elements
- Compare product against double the sum of all elements