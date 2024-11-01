results = [8, 10, 9, 6, 10]  # Пример значений, которые дают среднее 8.6

total = sum(results)
count = len(results)
average = total / count
min_score = min(results)
max_score = max(results)

print("Среднее арифметическое результатов выстрелов:", round(average, 1))
print("Наименьшее количество очков за выстрел:", min_score)
print("Наибольшее количество очков за выстрел:", max_score)
