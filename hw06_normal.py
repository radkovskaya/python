# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
# (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
# (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, fname):
        self.name = name
        self.surname = surname
        self.fname = fname
    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.fname
    def get_short_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.fname[0]+ '.'

class Student(Person):
    def __init__(self, name, surname, fname, class_room, father_name, mother_name):
        Person.__init__(self, name, surname, fname)
        self.class_room = class_room
        self.father_name = father_name
        self.mother_name = mother_name
    def __repr__(self):
        return self.surname + ' ' + self.name[0] + '.' + self.fname[0] + '.'


class Teacher(Person):
    def __init__(self, name, surname, fname, lesson, teach_classes):
        Person.__init__(self, name, surname, fname)
        self.teach_classes = teach_classes
        self.lesson = lesson
    def __repr__(self):
        return self.surname + ' ' + self.name + ' ' + self.fname

class ClassRoom:
    def __init__(self, num, char):
        self.num = num
        self.char = char

    def as_string(self):
        return "{}{}".format(self.num, self.char)

students = [Student("Александр", "Иванов", 'Васильевич', ClassRoom(8, "А"), "Василий Иванов", "Иванова Татьяна" ),
            Student("Петр", "Сидоров", 'Алексеевич', ClassRoom(8, "Б"), " Алексей Сидоров", "Кузнецова Изольда"),
            Student("Иван", "Петров", 'Антонович', ClassRoom(8, "А"), " Антон Петров", "Петрова Василиса"),
            ]
teachers = [Teacher("Борис", "Аносов", "Дмитриквич", "История", [ClassRoom(7, "А"), ClassRoom(5, "А")]),
             Teacher("Василий", "Макаров", "Федорович", "Литература", [ClassRoom(5, "А"), ClassRoom(8, "Б")]),
             Teacher("Маркелова", "Анна", "Анатольевна", "Математика", [ClassRoom(4, "А"), ClassRoom(8, "А")]),
             ]

def all_class():
    all_class = set()
    for student in students:
        all_class.add(student.class_room.as_string())
    return all_class

def students_class(class_room):
    student_class = []
    for student in students:
        if student.class_room.as_string() == class_room.as_string():
            student_class.append(student)
    return student_class

def teachers_class(class_room):
    teachers_class = []
    for teacher in teachers:
        for element in teacher.teach_classes:
            if element.as_string() == class_room.as_string():
                teachers_class.append(teacher)
    return teachers_class


def student_parent(name_student):
    mother = ""
    father = ""
    for student in students:
        if student.name == name_student[1] and student.surname == name_student[0] and student.fname == name_student[2]:
            mother = student.mother_name
            father = student.father_name
    return mother, father

def lessons_student(name_student):
    lessons = []
    for student in students:
        if student.name == name_student[1] and student.surname == name_student[0] and student.fname == name_student[2]:
            for teacher in teachers:
                for element in teacher.teach_classes:
                    if student.class_room.as_string() == element.as_string():
                        lessons.append(teacher.lesson)
    return lessons



print("Список всех классов школы, в которых учатся ученики :", all_class())
class_room = ClassRoom(8, "А")
print("Спиок всех учеников, которые учатся в классе", class_room.as_string(), students_class(class_room))
name_student = ["Сидоров", "Петр", "Алексеевич"]
print("Ученик {} {} {} изучает предметы, {}".format(name_student[1], name_student[0], name_student[2], lessons_student(name_student)))
print("Родителями ученика {} {} {} являются {}".format(name_student[1], name_student[0], name_student[2], student_parent(name_student)))
print("Спиок учителей, которые преподают в классе" , class_room.as_string(), teachers_class(class_room))

