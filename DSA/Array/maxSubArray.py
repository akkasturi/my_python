
def max_sub_array_brute(nums):
    size = len(nums)
    sum = 0
    max_sum = sum
    max_sum_index = 0

    print(f"Input: {nums}")
   # For each element go through its entire sub array, keep on adding. 
   # Keep tracking sum till current element and sum till previous element
   # if new sum is less than the previous sum, the save the previous sum index
   # that is our end index for this sub array.
    for index in range(size):
        prev_sum = nums[index]
        sum = nums[index]
        for index2 in range(index+1, size):
            sum += nums[index2]
            if(sum < prev_sum):
                good_max_index = index2 - 1
            else:
                prev_sum = sum
                good_max_index = index2 

        print(f"\tDebug: Max Sum: {prev_sum}, Sub Array [{index}:{good_max_index}]")
        if(prev_sum > max_sum):
            max_sum = prev_sum
            max_sum_index = index 

    print(f"\tOutput: Max Sum: {max_sum} for sub array starting at index: {max_sum_index}\n")


# main
nums = [1,2,3,4]
max_sub_array_brute(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sub_array_brute(nums)
