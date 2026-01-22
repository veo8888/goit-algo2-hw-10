# Definition of the Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    """
    Greedy algorithm for covering a set of subjects by teachers.

    At each step, we choose the teacher who can cover the most
    of the uncovered subjects. If the number is the same, we choose the youngest.
    """
    # Copying multiple objects without changing the original
    uncovered_subjects = set(subjects)

    # List of selected teachers
    selected_teachers = []

    # Resetting assigned subjects for all teachers.
    for teacher in teachers:
        teacher.assigned_subjects = set()

    while uncovered_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            # Find the subjects that this teacher can cover from the uncovered ones
            coverage = teacher.can_teach_subjects & uncovered_subjects

            # Skip teachers who cannot cover any subject
            if not coverage:
                continue

            # Choose the teacher with the largest coverage
            # With the same coverage - the youngest
            if best_teacher is None:
                best_teacher = teacher
                best_coverage = coverage
            elif len(coverage) > len(best_coverage):
                best_teacher = teacher
                best_coverage = coverage
            elif len(coverage) == len(best_coverage) and teacher.age < best_teacher.age:
                best_teacher = teacher
                best_coverage = coverage

        # If no teacher is found, it is impossible to cover all subjects
        if best_teacher is None:
            return None

        # Add a teacher to the list and assign subjects to him/her
        best_teacher.assigned_subjects = best_coverage
        selected_teachers.append(best_teacher)

        # Removing covered objects
        uncovered_subjects -= best_coverage

    return selected_teachers


if __name__ == "__main__":
    # A set of objects
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Creating a list of teachers
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Calling the schedule creation function
    schedule = create_schedule(subjects, teachers)

    # Schedule output
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
