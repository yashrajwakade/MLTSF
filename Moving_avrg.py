# Data of 10 days for jalebi
data = [9, 11, 13, 8, 10, 12, 7, 14, 9, 11]

def first_order_moving_average(data):
    
    if len(data) < 2:
        return []
    
    result = []
    
    for i in range(1, len(data)):
        
        avg = (data[i] + data[i-1]) / 2
        result.append(avg)
    return result

def second_order_moving_average(data):
    
    if len(data) < 3:
        return []

    result = []
    
    for i in range(2, len(data)):
        
        avg = (data[i] + data[i-1] + data[i-2]) / 3
        result.append(avg)
    return result


first_order_ma = first_order_moving_average(data)
second_order_ma = second_order_moving_average(data)


print(f"Original data: {data}")
print(f"1st-order Moving Average:", first_order_ma)
print(f"2nd-order Moving Average:", second_order_ma)