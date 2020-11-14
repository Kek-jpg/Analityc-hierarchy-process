n = int(input('Введи количество критериев: '))

matrix=[]
sum = 0
str_sum = 0
total_sum = 0
weighting_factor = 0
for i in range(n):
    matrix.append([]) 
    for j in range(n): 
        if i == j:
            matrix[i].append(round(1, 2))
        elif i > j:
            matrix[i].append(round(1/matrix[j][i], 2))
        else:
            element = float (input('Введите коэффициент для сравнения ' + str(i+1) + '-го критерия с критерием ' + str(j+1) + " "))
            matrix[i].append(round(element, 2))

for i in range(n):
    print(matrix[i])
print()
for i in range(n):
    for j in range(n):
        total_sum += matrix[i][j]

for i in range(n):
    for j in range(n):
        sum += matrix[i][j]
        if j == n-1:
            str_sum = sum
            print('Весовой коэфициент ' + str((i+1)) + '-го критерия: ' + str(round((str_sum/total_sum), 2)))
            sum = 0