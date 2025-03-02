'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

'''

''' Logic
    Create Prefix product array, For an index it contains product of all values before that index.
      - this is created by traversing main array from left to right.
    Create Suffix product array, For an index it contains product of all values after that index.
      - this is created by traversing main array from right to left.
      - this Suffic product array can be optimized by using single variable only.

    Multiple these two arrays get the final product array.
    
    As we traversed main array only twice which is O(2n) and 2 constant can be ignored, it is 
    effectively O(n)
    with Space complextity of O(n) due to prefix product array.

    This can be further optimized if we used the prefix product array itself for final result.
'''


def get_prefix_products(nums, prefix_products):
    index = 1
    
    while index < len(nums):
        prefix_products[index]  = prefix_products[index-1] * nums[index-1] 
        index += 1

    

def get_products(nums, prefix_products, products):
    suffix_product = 1
    index = len(nums) - 1

    while index >= 0:
        products[index]  = prefix_products[index] * suffix_product
        suffix_product = suffix_product * nums[index]
        index -= 1

def get_products_optimized(nums, prefix_products):
    suffix_product = 1
    index = len(nums) - 1

    while index >= 0:
        prefix_products[index]  = prefix_products[index] * suffix_product
        suffix_product = suffix_product * nums[index]
        index -= 1

    print(f"\tOptimized output: {prefix_products}")


def get_array_product_except_self(nums):
    num_len = len(nums)
    prefix_products = [1] * num_len
    products = [1] * num_len
    run_optimized = True

    # Create Prefix product array.
    get_prefix_products(nums, prefix_products)

    if(run_optimized):
        print(f"Input: {nums}")
        get_products_optimized(nums, prefix_products)
    else:
        get_products(nums, prefix_products, products)
       
        print(f"Input: {nums}")
        print(f"\tPrefixes: {prefix_products}")
        print(f"\tOutput: {products}")


#main
arr_nums2 = [1,2,3,4]
get_array_product_except_self(arr_nums2)

arr_nums = [5,2,3,4,10]
get_array_product_except_self(arr_nums)


arr_nums3 = [-1,1,0,-3,3]
get_array_product_except_self(arr_nums3)

arr_nums4 = [1,2]
get_array_product_except_self(arr_nums4)

