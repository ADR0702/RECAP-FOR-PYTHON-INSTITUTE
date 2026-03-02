point=(4,7)

x, y =point
print(x)
print(y)

student = ("Maria", 10, "Matematica")

name, grade, discipline = student
print(grade)

x = 1, 2, 3

print(type(x))

data = ("Ion", 28, "Bucuresti")

nume, varsta, oras= data
print(oras)

anul_nasterii=1993

new_data=nume, varsta, oras, anul_nasterii
print(new_data)


locations={
    (45.76, 21.23): "Timisoara"
}

locations[(44.44 , 26.10)]="Bucuresti"
locations[(35.6892,51.3889 )] = "Teheran"
locations[(39.0392, 125.7625 )] = "Phenian"
locations[(39.9042, 116.4074)] = "Beijing"
locations[(59.9375, 30.3086 )] = "Sankt Petersburg"

print(locations[(45.76, 21.23)])