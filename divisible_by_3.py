def divisible_by_3(arr):
    sum_of_arr=sum(arr)
    if sum_of_arr%3==0:
        return 1 
    else:
        return 0
arr=list(map(int,input().split()))
print(divisible_by_3(arr))
