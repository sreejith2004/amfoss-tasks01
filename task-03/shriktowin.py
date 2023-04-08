def shrink_to_one_digit(n):
    # Keep track of the number of operations
    count = 0
    
    # Repeat the operation until n is a one-digit number
    while len(str(n)) > 1:
        # Compute the sum of the digits
        s = 0
        for digit in str(n):
            s += int(digit)
        
        # Update n and the operation count
        n = s
        count += 1
    
    # Return the number of operations
    return count

# Read the input number
n = input().strip()

# Compute the envelope number
env_num = shrink_to_one_digit(n)

# Print the envelope number
print(env_num)
