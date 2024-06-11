def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Get user input for 6 numbers
numbers = []
for i in range(6):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum and average using the functions
total_sum = calculate_sum(numbers)
avg = calculate_average(numbers)

print(f"Sum of the numbers is: {total_sum}")
print(f"Average of the numbers is: {avg}")

   
        
