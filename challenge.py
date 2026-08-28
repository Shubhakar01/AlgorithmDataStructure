from collections import deque

def distribute_queue(original_queue):
    # original_queue is a list or deque of customers in their original waiting order
    queue = deque(original_queue)
    
    shop_a = []
    shop_b = []
    
    turn = 0
    while queue:
        customer = queue.popleft()
        if turn % 2 == 0:
            shop_a.append(customer)
        else:
            shop_b.append(customer)
        turn += 1
        
    return shop_a, shop_b

# Example usage:
customers = [f"Customer {i}" for i in range(1, 7)]
shop_1, shop_2 = distribute_queue(customers)

print("Shop 1 gets:", shop_1)
print("Shop 2 gets:", shop_2)