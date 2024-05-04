
series_of_numbers = []

for i in range(5):
    series_of_numbers.append(int(input("Enter a number: ")))
        
print(f"Lowest Number: {min(series_of_numbers)}")
print(f"Highest Number: {max(series_of_numbers)}")
print(f"Total Numbers: {sum(series_of_numbers)}")
print(f"Average of Numbers: {sum(series_of_numbers)/len(series_of_numbers)}")
