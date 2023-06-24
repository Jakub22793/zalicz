numbers = input("Podaj liczby oddzielone spacją: ")
numbers_list = numbers.split()

sum = 0
count = 0

for num in numbers_list:
    sum += float(num)
    count += 1

average = sum / count
print("Średnia arytmetyczna wynosi:", average)
