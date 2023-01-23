# easy, array
# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    sum = 0
    largest = arr[0]
    smallest = arr[0]

    for i in range(len(arr)):
        sum += arr[i]
        if (arr[i] > largest):
            largest = arr[i]
        if (arr[i] < smallest):
            smallest = arr[i]

    print(sum - largest, sum - smallest)
