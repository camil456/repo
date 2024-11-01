numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)
filtered_numbers = [num for num in numbers if num is not None]
average = sum(filtered_numbers) / len(filtered_numbers)
average_rounded = round(average, 2)
numbers[missing_index] = average_rounded

print("Измененный список:", numbers)
