# FizzBuzz Debugging Guide

## Common Issues and Solutions

### Issue 1: Wrong Output for Multiples of 15
**Problem**: Numbers like 15, 30, 45 show "Fizz" instead of "FizzBuzz"

**Cause**: Wrong order of conditions
```python
# WRONG - This will never reach FizzBuzz
if i % 3 == 0:
    result.append("Fizz")
elif i % 5 == 0:
    result.append("Buzz")
elif i % 3 == 0 and i % 5 == 0:  # This will never execute!
    result.append("FizzBuzz")
```

**Solution**: Check most specific condition first
```python
# CORRECT
if i % 3 == 0 and i % 5 == 0:
    result.append("FizzBuzz")
elif i % 3 == 0:
    result.append("Fizz")
elif i % 5 == 0:
    result.append("Buzz")
```

### Issue 2: Numbers Appearing as Integers Instead of Strings
**Problem**: Output like `[1, 2, 'Fizz']` instead of `"1 2 Fizz"`

**Cause**: Not converting numbers to strings
```python
# WRONG
result.append(i)  # This adds integer
```

**Solution**: Convert to string
```python
# CORRECT
result.append(str(i))  # This adds string
```

### Issue 3: No Spaces Between Elements
**Problem**: Output like `"12Fizz4Buzz"` instead of `"1 2 Fizz 4 Buzz"`

**Cause**: Using wrong join method
```python
# WRONG
return "".join(result)
```

**Solution**: Join with spaces
```python
# CORRECT
return " ".join(result)
```

### Issue 4: Off-by-One Errors
**Problem**: Missing the last number or starting from 0

**Cause**: Wrong range parameters
```python
# WRONG - excludes the last number
for i in range(1, num):

# WRONG - starts from 0
for i in range(num + 1):
```

**Solution**: Correct range
```python
# CORRECT - includes 1 to num
for i in range(1, num + 1):
```

## Debugging Steps

### Step 1: Add Print Statements
```python
def StringChallenge(num):
    result = []
    
    for i in range(1, num + 1):
        print(f"Processing number: {i}")  # Debug line
        
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} is divisible by both 3 and 5")  # Debug line
            result.append("FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} is divisible by 3")  # Debug line
            result.append("Fizz")
        elif i % 5 == 0:
            print(f"{i} is divisible by 5")  # Debug line
            result.append("Buzz")
        else:
            print(f"{i} is regular number")  # Debug line
            result.append(str(i))
    
    print(f"Final result list: {result}")  # Debug line
    return " ".join(result)
```

### Step 2: Test with Small Numbers
Start with small inputs to verify logic:
```python
print(StringChallenge(1))   # Should be "1"
print(StringChallenge(3))   # Should be "1 2 Fizz"
print(StringChallenge(5))   # Should be "1 2 Fizz 4 Buzz"
print(StringChallenge(15))  # Should end with "FizzBuzz"
```

### Step 3: Check Divisibility Logic
Test the modulo operations separately:
```python
# Test divisibility
for i in [3, 5, 15, 30]:
    print(f"{i} % 3 = {i % 3}")
    print(f"{i} % 5 = {i % 5}")
    print(f"{i} divisible by 3: {i % 3 == 0}")
    print(f"{i} divisible by 5: {i % 5 == 0}")
    print("---")
```

### Step 4: Verify Expected vs Actual
Compare your output with the expected results:
```python
expected = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16"
actual = StringChallenge(16)

print("Expected:", expected)
print("Actual:  ", actual)
print("Match:   ", expected == actual)
```

## Quick Test Function
```python
def test_fizzbuzz():
    test_cases = [
        (3, "1 2 Fizz"),
        (5, "1 2 Fizz 4 Buzz"),
        (15, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz")
    ]
    
    for input_val, expected in test_cases:
        result = StringChallenge(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {input_val} - {status}")
        if status == "FAIL":
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")

test_fizzbuzz()
```