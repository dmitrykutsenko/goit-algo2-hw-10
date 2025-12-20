# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()
        self.reason = ""  # причина вибору

def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_cover = set()
        reason = ""

        for teacher in teachers:
            cover = teacher.can_teach_subjects & uncovered_subjects
            if len(cover) > len(best_cover):
                best_teacher = teacher
                best_cover = cover
                reason = "покриває найбільше непокритих предметів"
            elif len(cover) == len(best_cover) and len(cover) > 0:
                if best_teacher and teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_cover = cover
                    reason = "наймолодший серед кандидатів"

        if not best_teacher:
            return None

        best_teacher.assigned_subjects = best_cover
        best_teacher.reason = reason
        schedule.append(best_teacher)

        uncovered_subjects -= best_cover
        teachers.remove(best_teacher)

    return schedule


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        subject_assignment = {}
        for teacher in schedule:
            for subj in teacher.assigned_subjects:
                subject_assignment[subj] = teacher

        for subj in subjects:
            t = subject_assignment[subj]
            print(f"{subj}: {t.first_name} {t.last_name}, {t.age} років, email: {t.email} "
                  f"({t.reason})")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
