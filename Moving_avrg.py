# Data of 10 days for jalebi
data = [9, 11, 13, 8, 10, 12, 7, 14, 9, 11]

# We take window size as three
window = 3


def moving_average(data, window):
    n = len(data)
    result = []
    
    
    for i in range(n - window + 1):
        total = 0
        
        for j in range(window):
            total += data[i + j]
        avg = total / window
        result.append(avg)
    
    return result


m_a = moving_average(data, window)

print("Original data:", data)
print(f"{window}-day Moving Average:", m_a)
