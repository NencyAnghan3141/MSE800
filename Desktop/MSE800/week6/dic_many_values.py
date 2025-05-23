ids = [1, 2, 3]
names = ['a', 'b', 'c']
grades = [90, 80, 70]

students = {
    id: {
        'name': name,
        'grade': grade
    }
    for id, name, grade in zip(ids, names, grades)
}
print(students)
