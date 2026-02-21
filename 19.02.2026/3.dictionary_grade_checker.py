students={
    "Ana": 9,
    "Ion": 7,
    "Maria": 10,
    "Paul": 6
}
the_best={}
total=0
has_perfect_grade=False
for student, grade in students.items():
    if grade > 8:
        the_best[student]=grade
    if grade == 10:
        print(f"the champion of the class is {student} with the grade {grade}")
        has_perfect_grade=True
    total+=grade

print(f"The grades higher than 8 in the class are: {the_best}") 
media=total / len(students)
print(f"the average grade of the class is {media} ")
if has_perfect_grade:
    print("We have a perfect student!")
else:
    print("This class is full of idiots!")
