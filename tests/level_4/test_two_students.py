from functions.level_4.two_students import Student, get_student_by_tg_nickname

def test__get_student_by_tg_nickname__return_user_when_valid_id_provided(sample_students):
    result = get_student_by_tg_nickname("john_doe", sample_students)
    assert result == Student("John", "Doe", "@john_doe")

def test__get_student_by_tg_nickname__return_none_when_user_not_in_list(sample_students):
    result = get_student_by_tg_nickname("nonexistent_user", sample_students)
    assert result is None

def test__get_student_by_tg_nickname__return_none_when_user_has_no_telegram_handler(sample_students):
    result = get_student_by_tg_nickname("jane_smith", sample_students)
    assert result is None

def test__get_student_by_tg_nickname__return_first_student_when_multiple_students_with_same_handler(sample_students):
    sample_students.append(Student("Jane", "Doe", "@john_doe"))
    result = get_student_by_tg_nickname("john_doe", sample_students)
    assert result == Student("John", "Doe", "@john_doe")

