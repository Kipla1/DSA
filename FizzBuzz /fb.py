def StringChallenge(num):
    result = []
    
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    return " ".join(result)

# Test cases
# print(StringChallenge(3))   # Expected: "1 2 Fizz"
# print(StringChallenge(16))  # Expected: "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16"
print(StringChallenge(input()))  # For interactive testing