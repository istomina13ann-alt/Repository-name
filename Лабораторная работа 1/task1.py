numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len_1 = len(numbers)
numbers[4] = 0
sum_1 = sum(numbers) - numbers[4]
sr_1 = sum(numbers) / len(numbers)
numbers[4] = sr_1
numbers_1 = numbers
print("Измененный список:", numbers_1)
