# Approach 1: 2 for loops , compare each number with every other number.
#            Not good Time Complexity. Time Complexity : O(n²) , Space Complexity: O(1) 

# Approach 2: If use addtional space O(n), Time Complexity can be : O(n²)
#             That is use Sets


def check_and_update_visited(visited, element):
 if element in visited:
     return True 
 else:
     visited.add(element)
 return False 


def find_duplicate(numbers):
    visited = set()
    duplicate_found = False
    print(f"Finding Duplicate in {numbers}")

    for number in numbers:
        if(check_and_update_visited(visited, number)):
            print(f"\tDuplicate number {number} exists!")
            duplicate_found = True

    if(duplicate_found == False):
        print(f"\tNo Duplicate number exists!")


## main 
numbers = [88,22,4,6,2,1,88,99,457]
numbers2 = [88,22,4,6,2,1,99,457]
numbers3 = [1,1,1,1,1,3,3,3,4,4]

find_duplicate(numbers)
find_duplicate(numbers2)
find_duplicate(numbers3)
