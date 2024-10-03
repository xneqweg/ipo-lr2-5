stud_cl1 = int(input("Введите количество учеников в 1-м классе: "))
stud_cl2 = int(input("Введите количество учеников во 2-м классе: "))
stud_cl3 = int(input("Введите количество учеников в 3-м классе: "))

total_students = stud_cl1 + stud_cl2 + stud_cl3

needed_desks = total_students // 2 + (total_students % 2)

print(f"Необходимо закупить {needed_desks} парт.")