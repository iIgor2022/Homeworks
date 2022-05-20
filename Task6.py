class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lektor, course, grade):
        if isinstance(lektor, Lecturer) and course in self.courses_in_progress and course in lektor.courses_attached:
            if course in lektor.grades:
                lektor.grades[course] += [grade]
            else:
                lektor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        rate = 0
        for key, values in self.grades.items():
            rate_course = 0
            for value in values:
                rate_course += value
            rate += rate_course / len(values)
        if len(self.grades):
            return rate / len(self.grades)
        else:
            return 0;

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_rating():0.3f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Класс {other.__class.__name__} не студент')
            return
        return self._average_rating() < other._average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating():0.3f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Класс {other.__class.__name__} не лектор')
            return
        return self._average_rating() < other._average_rating()

    def _average_rating(self):
        rate = 0
        for key, values in self.grades.items():
            rate_course = 0
            for value in values:
                rate_course += value
            rate += rate_course / len(values)
        if len(self.grades):
            return rate / len(self.grades)
        else:
            return 0;


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Java')

student1 = Student('Adam', 'Sandler', 'gn')
student1.courses_in_progress += ['Python']
student1.add_courses('GIT')


student2 = Student('Bruce', 'Willis', 'gn')
student2.courses_in_progress += ['Python']
student2.add_courses('JavaScript')


reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Java']

reviewer2 = Reviewer('John', 'Smith')
reviewer2.courses_attached += ['JavaScript', 'Python', 'Java']

lektor1 = Lecturer('Andrew', 'Lawson')
lektor1.courses_attached += ['JavaScript', 'Python']

lektor2 = Lecturer('Phillip', 'Austin')
lektor2.courses_attached += ['Java', 'Scala', 'Python', 'Rust']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 7)
reviewer1.rate_hw(best_student, 'Python', 4)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 5)

best_student.rate_hw(lektor1, 'Python', 10)
student1.rate_hw(lektor1, 'Python', 5)
student2.rate_hw(lektor1, 'Python', 8)

best_student.rate_hw(lektor2, 'Python', 2)
student1.rate_hw(lektor2, 'Python', 7)
student2.rate_hw(lektor2, 'Python', 6)

print(best_student.grades)
print(reviewer1)
print(lektor1)
print(best_student)
print(reviewer2)
print(lektor1 < lektor2)
print(best_student < student1)



def aver_rate_students(students, course):
    aver_rate = 0
    count_rates = 0
    for student in students:
        if course in student.grades.keys():
            for value in student.grades[course]:
                aver_rate += value
                count_rates += 1
    if count_rates:
        aver_rate = aver_rate / count_rates
    else:
        aver_rate = 0
    print(f'Средняя оценка студентов за курс "{course}" составляет {aver_rate:0.3f}')

def aver_rate_lector(lektors, course):
    aver_rate = 0
    count_rates = 0
    for lektor in lektors:
        if course in lektor.grades.keys():
            for value in lektor.grades[course]:
                aver_rate += value
                count_rates += 1
    if count_rates:
        aver_rate = aver_rate / count_rates
    else:
        aver_rate = 0
    print(f'Средняя оценка лекторов за курс "{course}" составляет {aver_rate:0.3f}')

aver_rate_students([student2, best_student], 'Python')
aver_rate_lector([lektor1, lektor2], 'Python')