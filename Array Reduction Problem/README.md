# Array Challenge Instructions

## Function Specification
**Function Name:** `ArrayChallenge(arr)`

**Input:** An array of positive integers stored in `arr`

## Algorithm Description
Perform the following algorithm continuously:
1. Get the difference of adjacent integers to create a new array of integers
2. Do the same for the new array until a single number is left
3. Return that number

## Example Walkthrough
If `arr` is `[4, 5, 1, 2, 7]`:

**Step 1:** Taking the difference of each pair of elements produces the following new array: `[1, 4, 1, 5]`
- |4 - 5| = 1
- |5 - 1| = 4  
- |1 - 2| = 1
- |2 - 7| = 5

**Step 2:** Do the same for this new array to produce `[3, 3, 4]`
- |1 - 4| = 3
- |4 - 1| = 3
- |1 - 5| = 4

**Step 3:** Continue: `[0, 1]`
- |3 - 3| = 0
- |3 - 4| = 1

**Step 4:** Final step: `[1]`
- |0 - 1| = 1

**Result:** The program should return the number `1` because that is what's left at the end.

## Test Case
**Input:** `[5, 7, 16, 1, 2]`  
**Output:** `7`