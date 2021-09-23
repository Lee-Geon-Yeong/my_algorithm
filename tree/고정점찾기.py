N=int(input())
array=list(map(int, input().split()))

def fix(array, start, end):
    while(start<=end):
        mid=(start+end)//2
        if array[mid]==mid:
            return mid
        elif array[mid]<mid:
            start=mid+1
        else:
            end=mid-1
    return -1    

result=fix(array, 0, N-1)
print(result)        

# from bisect import bisect_left, bisect_right
# n = int(input())
# arr = list(map(int, input().split()))

# def bisect_cnt(arr, left, right):
#     left = bisect_left(arr, left)
#     right = bisect_right(arr, right)
#     return right, left

# result = -1
# for fp in arr:
#     right, left = bisect_cnt(arr, fp, fp)
#     if left == fp:
#         result = fp

# print(result)