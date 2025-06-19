def ArrayChallenge(arr):
    while len(arr) > 1:
        new_arr = []
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            new_arr.append(diff)
        arr = new_arr
    return arr[0]