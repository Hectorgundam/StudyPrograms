# Even and Odd Node Reorganization
# Python Program 

# Program that takes in a linked list of numbers and reorganizes the nodes such that the even positioned nodes are 
# in front of the odd positioned nodes 
# In this case we are not hard coding or updating the values inside the nodes, they should only be reorganized 

# Practice help using geeksforgeeks.org for reference help 
# Python program to rearrange link list in place

# Notes: 
# self is a reference to the instance of the class where a method is defined. 
    # It's a convention in Python OOP
# head is a parameter representing the head node of the linked list 
# node is a parameter representing the starting node of th elinked list or a subsection that you want to print
# new_data is a parameter that will hold the data that needs to be inserted into a new node at the beginning of the list 

# Node class
class Node: 

    # Creating object and initializing its attributes
    def __init__(self, d): 

        self.data = d 
        self.next = None 

# LinkedList class
class LinkedList: 

    # Creating an object and initializing its attributes 
    def __init__(self):
        
        self.head = None 

    # Defining a function/method called newNode 
    # Function used to create a new node 
    def newNode(self, key): 

        # Creating a new instance of the Node class 
        # Calls the constructor Node passing key as the argument and assigns the values to temp 
        temp = Node(key)

        # Setting the contents of self's next as None 
        # next being the next node in a linked list 
        self.next = None 

        # Returning the contents of temp, which is a newly created node 
        return temp 
    
    # Defining a function/method called rearrangeEvenOdd
    # Function used to rearrange the nodes of the linked list so that all even positioned nodes are placed
    # before the odd positioned nodes 
    # (Important to note that it's NOT the contents of the nodes but the positions of the nodes)

    # Rearranging the given linked list such that all even positioned nodes are before the odd ones 
    # Returns a new head of linked list 
    def rearrangeEvenOdd(self, head): 

        # Remember
        # self is a reference to the instance of the class where a method is defined. 
            # It's a convention in Python OOP
        # head is a parameter representing the head node of the linked list 

        # Checking for a corner case - Empty List 
        # If the head of the linked list is None, then it means our list is empty
        if(self.head == None): 

            # We return None because there is nothing to rearrange in this case 
            return None 
        
        # odd will point to the head of the list
        # Will be used to traverse the odd-positioned nodes 
        odd = self.head 

        # even will point to the second node of the list 
        # Will be used to traverse the even-positioned nodes
        even = self.head.next 

        # Stores the head of the even-positioned nodes list
        # This will be used later to attach/connect this list at te end of the odd-positioned lists
        evenFirst = even 

        # Starting an infinite loop that will only stop once it reaches a break 
        while (1 == 1):

            # If there are no more nodes, then connect first node of even list to the last node of odd list 
            # It's basically checking if the end of the list has been reached of if there are no more even nodes
            if (odd == None or even == None or (even.next) == None): 

                # If the condition is met
                # We connect the last odd node to the head of the even list 
                odd.next = evenFirst 

                # Using break to exit the infinite loop 
                break 

            # Connecting odd nodes
            # Connecting the current odd node to the next node (by skipping the even node) 
            odd.next = even.next 

            # Moving the odd pointer to the next odd node (by skipping the even node pointer)
            odd = even.next 


            # If there are NO more even nodes after current odd 
            # It's basically checking if there are no more even nodes after the current odd node
            if (odd.next == None): 

                # If the condition is met 
                # We set even.next to None since tere are no more even nodes
                even.next = None 
                # And we connect the last odd node to the first even node 
                odd.next = evenFirst

                # Using break to exit the infinite loop
                break 

            # Connecting even nodes 
            # # Connecting the current even node to the next even node (by skippint the odd node)
            even.next = odd.next 

            # Moving the even pointer to the next even node (by skipping the odd node pointer)
            even = odd.next 

        # We return the head of the modified list
        return head 
    
    # Defining a function/method called printList
    # Function used to print a linked list in a readable format
    def printList(self,node): 

        # Remember 
        # self is a reference to the instance of the class where a method is defined. 
            # It's a convention in Python OOP
        # head is a parameter representing the head node of the linked list 
        # node is a parameter representing the starting node of the linked list or a subsection that you want to print

        # Cycle while node is not equal to None
        # It's basically running as long as the current node in the list is not the end of the list
        # None is being used to signify the end of the list in this case 
        while (node != None): 

            # Printing the data inside the node
            # The end="" helps us by not defaulting to the new-line when the printing is done, instead
            # it ends and allows the next print statement to be done in the same line 
            print(node.data, end = "")
            # Followed by printing -> and using end="" to end and allow the next print statement to 
            # be done in the same line 
            print(" -> ", end = "")

            # We update node to the next node in the linked list 
            node = node.next

        # After we exit the loop / when the node becomes None / when we reach the end of the linked list
        # Print NULL
        # Null in this case represents the end of the linked list 
        print("NULL")

    # Function to insert a new node at the beginning of the linked list 
    # Defining a function/method called push
    # Function used to create a new node with the new_data and add it to the beginning of the linked list, then
    # the new node becomes the new head of the list, and its next pointer is set to the previous head node
    # This helps in maintaining the continuity of the list 
    def push(self, new_data): 

        # Creating an instance of the Node class by calling the Node class and passing new_data as an argument and 
        # assigning the newly created node to the variable new_node 
        new_node = Node(new_data) 

        # new_node's next is set to point to the current head of the list 
        # With this, we insert a new_node before the current first node of the linked list 
        new_node.next = self.head 

        # We update self's head attribute, which is the attribute of the class instance that's pointing to the 
        # first node in the list so that it now points to new_node instead 
        self.head = new_node 

# Driver code 
        
# Creating a new instance of the LinkedList class and assigning it to the variable ll, which represents a linked list 
# The linked list ll is initially empty 
ll = LinkedList()

# Calling the push method/function of the LinkedList instance ll 
# Each time it's called a new node is inserted at the beginning of the list 
# Remember that because each node is being inserted at the beginning of the list, the final order we get is 1, 2, 3, 4, 5
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

# Using this as a spacer to ease readability of our output for now
print()

# Stating that the initial list will be printed as it was created  
print("Given Linked List:") 

# Calling the printList method/function of the LinkedList instance ll 
# This will print the elements of the linked list starting from the head node 
# At this point no changes have been made to the list and it's expected to print as 1 -> 2 -> 3 -> 4 -> 5 -> NULL
ll.printList(ll.head)

# Using this as a spacer to ease readability of our output for now
print()

# Calling the rearrangeEvenOdd method/function of the LinkedList instance ll 
# We are rearranging the linked list so that all nodes in even positions are placed in front of the odd positioned ones
# Once rearranged, the head of the rearranged list is returned and stored in the variable start 
start = ll.rearrangeEvenOdd(ll.head) 

# Stating that the rearranged list will be printed after it was rearranged 
print("Modified Linked List:")

# Calling the printList method/function of the LinkedList instance ll 
# This time it starts from start node, which is the head of the modified list 
# We are printing the elements in the rearranged list, which is expected to print as 2 -> 4 -> 1 -> 3 -> 5 -> NULL
ll.printList(start) 

# Using this as a spacer to ease readability of our output for now
print()
