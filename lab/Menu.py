"""
Menu driven program that uses:
  BinarySearchTree.py, Queue.py, Searching.py, SinglyLinkedList.py,
  Sortings.py, Stack.py, DoublyLinkedList.py

Keep this file in the same folder as the others. Your original files are NOT
modified. Because they run demo code / main() as soon as they are imported,
load_module() below only picks up their classes and functions (it skips
main() and the loose top-level code), so nothing runs or asks for input
unexpectedly.  Requires Python 3.10+ (Stack.py uses match/case).
"""

import ast
import os
import types

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def load_module(filename):
    """Load only imports, classes and functions (except main) from a file."""
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=path)

    keep = [
        node for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.ClassDef))
        or (isinstance(node, ast.FunctionDef) and node.name != "main")
    ]
    module = types.ModuleType(filename[:-3])
    code = compile(ast.Module(body=keep, type_ignores=[]), path, "exec")
    exec(code, module.__dict__)
    return module


def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


def read_int_list(prompt):
    while True:
        try:
            values = [int(x) for x in input(prompt).replace(",", " ").split()]
            if values:
                return values
            print("Enter at least one number.")
        except ValueError:
            print("Please enter only integers separated by spaces.")


def show_menu(title, options):
    print(f"\n===== {title} =====")
    for key, text in options:
        print(f"  {key} - {text}")
    return read_int("Enter your choice: ")


# --------------------------------------------------------------------------
# Load your modules
# --------------------------------------------------------------------------
bst_mod = load_module("BinarySearchTree.py")
queue_mod = load_module("Queue.py")
search_mod = load_module("Searching.py")
sll_mod = load_module("SinglyLinkedList.py")
sort_mod = load_module("Sortings.py")
stack_mod = load_module("Stack.py")
dll_mod = load_module("DoublyLinkedList.py")


# --------------------------------------------------------------------------
# Binary Search Tree
# --------------------------------------------------------------------------
def bst_menu(bst):
    options = [(1, "Insert"), (2, "Delete"), (3, "Display inorder"),
               (4, "Search"), (0, "Back")]
    while True:
        choice = show_menu("BINARY SEARCH TREE", options)
        if choice == 1:
            value = read_int("Enter value to insert: ")
            bst.insert(bst.root, value)
            print(f"Inserted {value}")
        elif choice == 2:
            value = read_int("Enter value to delete: ")
            if bst.search(value):
                # Re-assign root so deleting the root node works correctly
                bst.root = bst.delete(bst.root, value)
                print(f"Deleted {value}")
            else:
                print("Value not found")
        elif choice == 3:
            if bst.root is None:
                print("Tree is empty")
            else:
                print("Inorder: ", end="")
                bst.inorder(bst.root)
                print()
        elif choice == 4:
            value = read_int("Enter value to search: ")
            print("Found" if bst.search(value) else "Not found")
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Sorting
# --------------------------------------------------------------------------
def sorting_menu(state):
    options = [(1, "Bubble sort"), (2, "Selection sort"), (3, "Insertion sort"),
               (4, "Quick sort"), (5, "Merge sort"), (6, "Heap sort"),
               (7, "Change array"), (0, "Back")]
    while True:
        print(f"\nCurrent array: {state['array']}")
        choice = show_menu("SORTING", options)
        data = list(state["array"])  # work on a copy, original stays unsorted
        if choice == 1:
            print("Bubble sort:   ", sort_mod.bubble_sort(data))
        elif choice == 2:
            print("Selection sort:", sort_mod.selection_sort(data))
        elif choice == 3:
            print("Insertion sort:", sort_mod.insertion_sort(data))
        elif choice == 4:
            print("Quick sort:    ", sort_mod.quick_sort(0, len(data) - 1, data))
        elif choice == 5:
            print("Merge sort:    ", sort_mod.merge_sort(data))
        elif choice == 6:
            print("Heap sort:     ", sort_mod.heap_sort(data))
        elif choice == 7:
            state["array"] = read_int_list("Enter numbers separated by spaces: ")
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Searching
# --------------------------------------------------------------------------
def searching_menu(state):
    options = [(1, "Linear search"), (2, "Binary search"),
               (3, "Change array"), (0, "Back")]
    while True:
        print(f"\nCurrent array: {state['array']}")
        choice = show_menu("SEARCHING", options)
        if choice == 1:
            key = read_int("Enter element to search: ")
            found = search_mod.linear_search(state["array"], key)
            print("Element is Present" if found else "Element not present")
        elif choice == 2:
            key = read_int("Enter element to search: ")
            data = sorted(state["array"])  # binary search needs sorted data
            print(f"(Searching in sorted copy: {data})")
            found = search_mod.binary_search(data, 0, len(data) - 1, key)
            print("Element is Present" if found else "Element not present")
        elif choice == 3:
            state["array"] = read_int_list("Enter numbers separated by spaces: ")
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Stack
# --------------------------------------------------------------------------
def stack_menu(st):
    options = [(1, "Push"), (2, "Pop"), (3, "Peek"), (4, "Display"), (0, "Back")]
    while True:
        choice = show_menu("STACK", options)
        if choice == 1:
            value = read_int("Enter value to push: ")
            st.push(value)
            print(f"Pushed {value}")
        elif choice == 2:
            value = st.pop()
            print("Stack is empty" if value is None else f"Top value {value} removed")
        elif choice == 3:
            value = st.peek()
            print("Stack is empty" if value is None else f"Top of Stack is {value}")
        elif choice == 4:
            if st.head is None:
                print("Stack is empty")
            else:
                items, cur = [], st.head
                while cur is not None:
                    items.append(str(cur.data))
                    cur = cur.next
                print("Top -> " + " | ".join(items))
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Circular Queue
# --------------------------------------------------------------------------
def queue_menu(state):
    if state["queue"] is None:
        capacity = read_int("Enter queue capacity: ")
        while capacity <= 0:
            capacity = read_int("Capacity must be positive. Enter again: ")
        state["queue"] = queue_mod.CircularQueue(capacity)
    q = state["queue"]

    options = [(1, "Enqueue"), (2, "Dequeue"), (3, "Peek"), (4, "Display"),
               (0, "Back")]
    while True:
        choice = show_menu("CIRCULAR QUEUE", options)
        if choice == 1:
            value = read_int("Enter value to enqueue: ")
            before = q.count
            q.enqueue(value)  # prints "Queue is full" itself if needed
            if q.count > before:
                print(f"Enqueued {value}")
        elif choice == 2:
            value = q.dequeue()  # prints "Queue is empty" itself if needed
            if value is not None:
                print(f"Dequeued {value}")
        elif choice == 3:
            value = q.peek()
            print("Queue is empty" if value is None else f"Front is {value}")
        elif choice == 4:
            q.display()
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Singly Linked List
# --------------------------------------------------------------------------
def sll_menu(sll):
    options = [(1, "Insert at rear"), (2, "Insert after a value"),
               (3, "Delete node after a value"), (4, "Display"), (0, "Back")]
    while True:
        choice = show_menu("SINGLY LINKED LIST", options)
        if choice == 1:
            value = read_int("Enter value to insert: ")
            sll.insert_rear(value)
            print(f"Inserted {value}")
        elif choice == 2:
            pos = read_int("Insert after which value? ")
            value = read_int("Enter new value: ")
            sll.insert_after(pos, value)  # silently does nothing if pos missing
            print("Done (nothing happens if the value was not in the list)")
        elif choice == 3:
            pos = read_int("Delete the node after which value? ")
            try:
                sll.delete_after(pos)
                print("Done (nothing happens if the value was not in the list)")
            except AttributeError:
                print("There is no node after that value to delete")
        elif choice == 4:
            if sll.head is None:
                print("List is empty")
            else:
                sll.display()
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Doubly Linked List
# --------------------------------------------------------------------------
def dll_menu(dll):
    options = [(1, "Insert at front"), (2, "Insert at rear"),
               (3, "Insert after a value"), (4, "Delete from front"),
               (5, "Delete from rear"), (6, "Delete a value"), (7, "Search"),
               (8, "Display forward"), (9, "Display backward"), (0, "Back")]
    while True:
        choice = show_menu("DOUBLY LINKED LIST", options)
        if choice == 1:
            dll.insert_front(read_int("Enter value: "))
        elif choice == 2:
            dll.insert_rear(read_int("Enter value: "))
        elif choice == 3:
            pos = read_int("Insert after which value? ")
            value = read_int("Enter new value: ")
            if not dll.insert_after(pos, value):
                print("Value not found")
        elif choice == 4:
            value = dll.delete_front()
            print("List is empty" if value is None else f"Deleted {value}")
        elif choice == 5:
            value = dll.delete_rear()
            print("List is empty" if value is None else f"Deleted {value}")
        elif choice == 6:
            key = read_int("Enter value to delete: ")
            print("Deleted" if dll.delete_value(key) else "Value not found")
        elif choice == 7:
            key = read_int("Enter value to search: ")
            print("Found" if dll.search(key) else "Not found")
        elif choice == 8:
            dll.display_forward()
        elif choice == 9:
            dll.display_backward()
        elif choice == 0:
            return
        else:
            print("Invalid choice")


# --------------------------------------------------------------------------
# Main menu
# --------------------------------------------------------------------------
def main():
    # Data structures live here so they keep their contents between menus
    bst = bst_mod.BST()
    stack = stack_mod.Stack()
    sll = sll_mod.SLL()
    dll = dll_mod.DLL()
    queue_state = {"queue": None}
    array_state = {"array": [568, 367, 667, 353, 879, 323, 689, 122]}

    options = [(1, "Binary Search Tree"), (2, "Sorting"), (3, "Searching"),
               (4, "Stack"), (5, "Circular Queue"), (6, "Singly Linked List"),
               (7, "Doubly Linked List"), (0, "Exit")]
    while True:
        choice = show_menu("MAIN MENU", options)
        if choice == 1:
            bst_menu(bst)
        elif choice == 2:
            sorting_menu(array_state)
        elif choice == 3:
            searching_menu(array_state)
        elif choice == 4:
            stack_menu(stack)
        elif choice == 5:
            queue_menu(queue_state)
        elif choice == 6:
            sll_menu(sll)
        elif choice == 7:
            dll_menu(dll)
        elif choice == 0:
            print("Exiting")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
