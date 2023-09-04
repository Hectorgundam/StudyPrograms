# Binary Number in a Linked list
# A binary number is represented as a series of 0's and 1's. In this challenge, the series will be in the form of a singly-linked 
# list. Each node instance, a LinkedListNode, has a value, data, and a pointer to the next node, next. Given a reference to the head 
# of a singly-linked list, convert the binary number represented to a decimal number. 
# Example
# binary -> 0 -> 1 -> 0 -> 0 -> 1 -> 1 -> null
# Linked list corresponding to the binary number (010011)[2] or (10)[10]
# Function Description
# Complete the function getNumber in the editor below
# getNumber has the following parameters
# binary: reference to the head of a singly-linked list of binary digits
# Returns
# int: a (long integer)[10] representation of the binary number 
# Constraints
# 1 <= n <= 64
# All LinkedListNode.data E{01}
# The described (integer)[2] < 2^64
# Example
# binary[] size is 7
# n = 7
# 0 -> binary
# LinkedListNode.data = [0,0,1,1,0,1,0]
# Sample Output
# 26
# Explanation
# binary -> 0 -> 0 -> 1 -> 1 -> 0 -> 1 -> 0
# the linked list is given as inout.
# The linked list forms the binary number 0011010 -> (0011010)[2]= (26)[10]

# Complete the getNumber function below

# The function is expected to return a LONG_INTEGER
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter

# For your reference: 
# SinglyLinkedListNode: 
# int data 
# SinglyLinkedListNode next

def getNumber(binary):
    # Write your code here

    decimalVal = 0 

    currentPos = binary

    while currentPos:

        decimalVal = decimalVal * 2 + currentPos.data
        currentPos = currentPos.next

    return decimalVal




if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')

    fptr.close()