#avg grades

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))

dict_grades = {}
avg_grades =[]
for i in range(len(grades)):
    avg_grade = sum(grades[i])/len(grades[i])
    dict_grades[students_list[i]] = avg_grade

print(dict_grades)
