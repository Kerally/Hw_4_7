#7
mass_1 = []
mass_2 = []
mass_3 = []
mass_4 = []
mass_5 = []
mass_size_1 = int(input("Enter the size for first massive: "))
mass_size_2 = int(input("Enter the size for second massive: "))

# заповнюємо перший масив
for i in range(mass_size_1):
    mass_1.append(int(input("Enter the number for first massive: ")))

# заповнюємо другий масив
for i in range(mass_size_1):
    mass_2.append(int(input("Enter the number for second massive: ")))

for i in mass_1:
    # знаходимо спільні 
    if i in mass_2:
        mass_3.append(i)
    # знаходимо елменти які є тільки в першому
    if i not in mass_2:
        mass_4.append(i)
        mass_5.append(i)
# знаходимо різні елементи
for i in mass_2:
    if i not in mass_1:
        mass_5.append(i)

print("Same: ", mass_3)
print("Only in first: ", mass_4)
print("Different in both: ", mass_5)