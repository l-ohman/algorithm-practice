# easy, array
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem

def countingSort(arr):
    frequency_list = [0] * 100
    for i in range(len(arr)):
        frequency_list[arr[i]] += 1
    return frequency_list
