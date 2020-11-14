while True: # проверка ввода пользователя
                try:
                    n = int(input('Введи количество критериев: ')) # ввод количества критериев
                    if n < 1:
                        raise Exception()
                    break
                except Exception as e:
                    print('Данные введены неверно. Введите число (большее, чем 1)')
matrix=[] # создание списка для дальнейшей реализации матрицы
sum = 0 # объявление переменной для суммы элементов
str_sum = 0 # объявление переменной для суммы элементов в строке
total_sum = 0 # объявление переменной для суммы всех строк
weighting_factor = 0 # объявление переменной для весовых коэфициентов

for i in range(n): # цикл реализации матрицы
    matrix.append([]) 
    for j in range(n): 
        if i == j: # заполнение пересечений одинаковых критериев единицами
            matrix[i].append(round(1, 2))
        elif i > j: # расчёт значений, обратных введённым (там, где нужно)
            matrix[i].append(round(1/matrix[j][i], 2))
        else: # запрос ввода оценки критерия
            while True: # проверка ввода пользователя
                try:
                    element = float (input('Введите коэффициент для сравнения ' + str(i+1) + '-го критерия с '  + str(j+1) + '-ым критерием: '))
                    if element > 9:
                        raise Exception()
                    break
                except Exception as e:
                    print('Данные введены неверно. Введите число (меньшее, чем 9): ')
            matrix[i].append(round(element, 2))
print()
print("Матрица попарного сравнения критериев: ")

for i in range(n): # цикл печати матрицы (для наглядности)
    print(matrix[i])

print()
for i in range(n): # цикл вычисления суммы всех строк
    for j in range(n):
        total_sum += matrix[i][j]

for i in range(n): # цикл вычисления и печати весовых коэффициентов
    for j in range(n):
        sum += matrix[i][j]
        if j == n-1:
            str_sum = sum
            print('Весовой коэффициент ' + str((i+1)) + '-го критерия: ' + str(round((str_sum/total_sum), 2)))
            sum = 0