def relu(x):
    if x > 0:
        return x
    else:
        return 0
    pass
    
print(f"Input: 10, Output: {relu(10)}")