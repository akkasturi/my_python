'''
Practice - Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Your goal is to find the maximum profit you can make by choosing one day to buy a stock and a different future day to sell it.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

prices = [7,2,5,10,6,4]
#prices = [7,6,4,3,1]
#prices = [7,1,5,3,6,4]
profit = 0
min = prices[0]
arr_len = len(prices)
i = 1

# start from  
while i < arr_len:
    temp_profit = prices[i] - min
    if(temp_profit > profit):
        profit = temp_profit

    if(prices[i] < min):
        min = prices[i]

    i += 1

print(f"Maximum Profit is {profit}\n")



    
'''
Intuition
The problem aims to find the maximum profit that can be obtained by buying and selling a stock. The given solution seems to follow a simple approach of iterating through the prices, keeping track of the minimum buying price, and updating the profit whenever a higher selling price is encountered.


Approach
Initialize variables buy with the first element of the prices array and profit as 0.
Iterate through the prices starting from the second element.
Update the buy variable if the current price is lower than the current buying price.
Update the profit if the difference between the current price and the buying price is greater than the current profit.
Return the final profit.

Kadane's Algorithm
Kadane's Algorithm is a dynamic programming technique used to find the maximum subarray sum in an array of numbers. The algorithm maintains two variables: max_current represents the maximum sum ending at the current position, and max_global represents the maximum subarray sum encountered so far. At each iteration, it updates max_current to include the current element or start a new subarray if the current element is larger than the accumulated sum. The max_global is updated if max_current surpasses its value.

Relating with the Approach
In the provided approach for finding the maximum profit in stock prices, the algorithm can be seen as a variation of Kadane's Algorithm. Instead of finding the maximum subarray sum directly, it focuses on finding the maximum positive difference between consecutive elements (prices) in the array.

Here's how the approach relates to Kadane's Algorithm:

Initialization:

In Kadane's Algorithm, max_current and max_global are initialized to the first element of the array.
In the stock profit approach, buy is initialized with the first element of the prices array, and profit is initialized to 0.
Iteration:

Kadane's Algorithm iterates through the array, updating max_current based on the current element's value and deciding whether to start a new subarray.
The stock profit approach iterates through the prices array, updating buy when a lower price is encountered and treating the difference between the current price and buy as a potential profit.
Comparison and Update:

Kadane's Algorithm compares and updates max_current and max_global at each iteration.
The stock profit approach compares and updates profit whenever a positive difference between the current price and buy exceeds the current profit.
Complexity
Time complexity: O(n), where n is the length of the prices array. The algorithm iterates through the array once.
Space complexity: O(1), as only a constant amount of extra space is used.

'''
