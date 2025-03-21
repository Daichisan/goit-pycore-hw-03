import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    ticket_numbers = random.sample(range(min, max + 1), quantity)
    
    ticket_numbers.sort()
    
    return ticket_numbers

lottery_numbers = get_numbers_ticket(4, 33, 6)
print("Ваші лотерейні числа:", lottery_numbers)