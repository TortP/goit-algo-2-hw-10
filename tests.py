from task1 import Teacher, create_schedule


def print_test_header(test_name):

    print(f"{test_name}")



def print_schedule(schedule, subjects):
    if schedule:
        print("\nРозклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")
        
        print(f"Загальна кількість викладачів у розкладі: {len(schedule)}")
        
        all_covered = set()
        for teacher in schedule:
            all_covered.update(teacher.assigned_subjects)
        print(f"Покриті предмети: {', '.join(sorted(all_covered))}")
        
        if all_covered == subjects:
            print("Всі предмети успішно покрито!")
        else:
            print(f"Не покрито: {subjects - all_covered}")
    else:
        print("\n Неможливо покрити всі предмети наявними викладачами.")


def test_1_standard_case():
    print_test_header("ТЕСТ 1: Стандартний випадок (всі 6 викладачів)")
    
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', 
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', 
                {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', 
                {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', 
                {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', 
                {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', 
                {'Біологія'})
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)


def test_2_impossible_coverage():
    print_test_header("ТЕСТ 2: Неможливо покрити всі предмети")
    
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', 
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', 
                {'Хімія'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)


def test_3_age_priority():
    print_test_header("ТЕСТ 3: Пріоритет молодшого віку")
    
    subjects = {'Математика', 'Фізика'}
    teachers = [
        Teacher('Старший', 'Викладач', 50, 'old@example.com', 
                {'Математика', 'Фізика'}),
        Teacher('Молодший', 'Викладач', 30, 'young@example.com', 
                {'Математика', 'Фізика'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)
    
    if schedule and schedule[0].age == 30:
        print(" Коректно обрано молодшого викладача!")
    else:
        print(" Помилка: має бути обрано молодшого викладача!")


def test_4_minimize_teachers():
    print_test_header("ТЕСТ 4: Мінімізація кількості викладачів")
    
    subjects = {'Математика', 'Фізика', 'Хімія'}
    teachers = [
        Teacher('Універсал', 'Викладач', 40, 'universal@example.com', 
                {'Математика', 'Фізика', 'Хімія'}),
        Teacher('Математик', 'Спеціаліст', 35, 'math@example.com', 
                {'Математика'}),
        Teacher('Фізик', 'Спеціаліст', 38, 'physics@example.com', 
                {'Фізика'}),
        Teacher('Хімік', 'Спеціаліст', 42, 'chem@example.com', 
                {'Хімія'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)
    
    if schedule and len(schedule) == 1:
        print(" Оптимально: використано лише 1 викладача!")
    else:
        print(f" Використано {len(schedule) if schedule else 0} викладачів (очікувалось 1)")


def test_5_super_teacher():
    print_test_header("ТЕСТ 5: Один супервикладач на всі предмети")
    
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher('Супер', 'Універсал', 45, 'super@example.com', 
                {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)


def test_6_empty_subjects():
    print_test_header("ТЕСТ 6: Порожня множина предметів")
    
    subjects = set()
    teachers = [
        Teacher('Викладач', 'Один', 40, 'teacher@example.com', 
                {'Математика', 'Фізика'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    
    if schedule is not None and len(schedule) == 0:
        print("\n Правильно оброблено порожню множину предметів")
        print("Розклад: порожній (немає предметів для викладання)")
    else:
        print("\n Помилка обробки порожньої множини")


def test_7_overlapping_subjects():
    print_test_header("ТЕСТ 7: Перевірка жадібного вибору")
    
    subjects = {'Математика', 'Фізика', 'Хімія', 'Біологія'}
    teachers = [
        Teacher('Викладач А', 'Перший', 30, 'a@example.com', 
                {'Математика', 'Фізика', 'Хімія'}),
        Teacher('Викладач Б', 'Другий', 35, 'b@example.com', 
                {'Біологія'}),
        Teacher('Викладач В', 'Третій', 40, 'c@example.com', 
                {'Математика', 'Біологія'}),
    ]
    
    schedule = create_schedule(subjects, teachers.copy())
    print_schedule(schedule, subjects)
    
    if schedule and len(schedule) == 2:
        print(" Жадібний алгоритм працює оптимально!")


if __name__ == '__main__':

    print("ЗАПУСК СИСТЕМИ ТЕСТУВАННЯ РОЗКЛАДУ ЗАНЯТЬ")

    
    test_1_standard_case()
    test_2_impossible_coverage()
    test_3_age_priority()
    test_4_minimize_teachers()
    test_5_super_teacher()
    test_6_empty_subjects()
    test_7_overlapping_subjects()
    

    print("ВСІ ТЕСТИ ЗАВЕРШЕНО")

