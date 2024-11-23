grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(students)

average_grage = {}

for i in range(len(grades)) :
    students_grades = grades [i]
    students_name = students_list[i]
    average_grage[students_name] = sum(students_grades) / len(students_grades)

print(average_grage)