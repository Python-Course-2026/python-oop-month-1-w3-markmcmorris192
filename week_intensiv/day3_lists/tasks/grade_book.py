class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self):
        self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        best_avarage = 0
        best_student = None
        for name, grades in self.students.items():
            avarage = sum(grades) / len(grades)
            if avarage > best_avarage:
                best_avarage = avarage
                best_student = name
        return best_student
