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
Using recursion, we visit each index in array.
Each recursive call works on an index of array from left to right.


Idea is to get product of all the values before and after of current frame.

To do that, while going left to right, In Each frame we are trying to collect:
   i) value at previous index of array,
   ii) product of all values before the previous index

At this point we pending the product of all the values of right side of array.

Now, when last frame (array index) is reached. We have:
    i) In last frame , prodcut of all the previous values, which we save in last index.
    ii) While unwinding(returning) pass current frame(index) value, which is use to 
        derive the product of right side values with current (which has product of left side values)
        except the current frame value. 

samajh sako to hame bhi jara samjhana.
Bye god !! maine hi kiya hai ye khud se.
'''


def get_product(product, index, nums, answers):
    if(index == 0 and len(nums) == 1):
        answers[index] = 1
        return 1
    elif(index == (len(nums)-1)): 
    #end of array. do prodcut of value at previous index with product of all previous values
    # we have to skip that last value
        answers[index] = product * nums[index-1]
        return nums[index]
    else: 
        if(index == 0):
            product = product * 1
        else:
            # take the product of value at previous index with the product of all previous values
            product = product * nums[index-1]

        #pass the product so far calculated to next frame
        temp_product = get_product(product, index+1, nums, answers)

        # Here, we are multiplying products of left and right side of current frame and 
        # avoiding current index value.
        product = product * temp_product 
        answers[index] = product

        #notice, how we are avoiding current index value in product of current index,
        #        just passing it to previous frame.
        return temp_product * nums[index] 

def get_array_product_except_self(nums):
    product = 1
    index = 0
    num_len = len(nums)
    answers = [1] * num_len
    get_product(product, index, nums, answers)
    print(answers)


#main
nums = [5,2,3,4,10]
get_array_product_except_self(nums)

nums2 = [1,2,3,4]
get_array_product_except_self(nums2)

nums3 = [-1,1,0,-3,3]
get_array_product_except_self(nums3)

nums4 = [1,2]
get_array_product_except_self(nums4)
