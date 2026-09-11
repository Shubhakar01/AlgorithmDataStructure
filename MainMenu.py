import Stack
import Queue
import SinglyLinkedList
import DoublyLinkedList
import CircularQueue
import  BinarySearchTree

while(True):
    print(
        "Enter 1 for Stack\n",
        "Enter 2 for Queue\n",
        "Enter 3 for Singly Linked List\n",
        "Enter 4 for Doubly Linked List\n",
        "Enter 5 for Circular Queue\n",
        "Enter 6 for Binary Search Tree",
        )
    user_choice = int(input())
    match user_choice :
        case 1:
            stck= Stack()
            print("Enter i for push, enter p for pop, Enter d for display, Enter")