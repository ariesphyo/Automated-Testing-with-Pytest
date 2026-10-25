import pytest

from src.student_manager import Student, StudentManager


def test_student_initializes_attributes_and_independent_grades(sample_student):
    assert sample_student.student_id == "S001"
    assert sample_student.name == "Ada Lovelace"
    assert sample_student.email == "ada@example.com"
    assert sample_student.grades == {}

    other_student = Student("S002", "Grace Hopper", "grace@example.com")
    other_student.add_grade("CS101", 90)
    assert sample_student.grades == {}


@pytest.mark.parametrize(
    ("student_id", "name", "email"),
    [
        ("", "Ada Lovelace", "ada@example.com"),
        (None, "Ada Lovelace", "ada@example.com"),
        ("S001", "", "ada@example.com"),
        ("S001", None, "ada@example.com"),
        ("S001", "Ada Lovelace", ""),
        ("S001", "Ada Lovelace", None),
        ("S001", "Ada Lovelace", "invalid-email"),
    ],
)
def test_student_rejects_invalid_identity_attributes(student_id, name, email):
    with pytest.raises(ValueError):
        Student(student_id, name, email)


@pytest.mark.parametrize(("score", "expected"), [(0, 0.0), (100, 100.0), (82.5, 82.5)])
def test_student_add_grade_accepts_scores_inclusive_of_bounds(
    sample_student, score, expected
):
    sample_student.add_grade("MATH101", score)
    assert sample_student.grades["MATH101"] == expected


@pytest.mark.parametrize("score", [-0.01, 100.01])
def test_student_add_grade_rejects_scores_outside_bounds(sample_student, score):
    with pytest.raises(ValueError):
        sample_student.add_grade("MATH101", score)


@pytest.mark.parametrize("score", ["90", None, True, False])
def test_student_add_grade_rejects_non_numeric_scores(sample_student, score):
    with pytest.raises(TypeError):
        sample_student.add_grade("MATH101", score)


@pytest.mark.parametrize("course_code", ["", None, 101])
def test_student_add_grade_rejects_invalid_course_code(sample_student, course_code):
    with pytest.raises(ValueError):
        sample_student.add_grade(course_code, 90)


@pytest.mark.parametrize(
    ("score", "expected_gpa"),
    [(90, 4.0), (80, 3.0), (70, 2.0), (60, 1.0), (59.99, 0.0)],
)
def test_student_gpa_maps_grade_bracket_boundaries(sample_student, score, expected_gpa):
    sample_student.add_grade("COURSE", score)
    assert sample_student.get_gpa() == expected_gpa


def test_student_gpa_averages_course_points(sample_student):
    sample_student.add_grade("COURSE101", 95)
    sample_student.add_grade("COURSE102", 85)
    sample_student.add_grade("COURSE103", 75)
    assert sample_student.get_gpa() == 3.0


def test_student_gpa_is_zero_without_grades(sample_student):
    assert sample_student.get_gpa() == 0.0


def test_empty_manager_starts_with_no_students(empty_manager):
    assert empty_manager.get_total_students() == 0
    assert empty_manager.get_all_students() == []


def test_student_manager_adds_student_instance(empty_manager, sample_student):
    added = empty_manager.add_student(sample_student)
    assert added is sample_student
    assert empty_manager.get_student("S001") is sample_student
    assert empty_manager.get_total_students() == 1


def test_student_manager_adds_student_from_parameters(empty_manager):
    added = empty_manager.add_student("S002", "Grace Hopper", "grace@example.com")
    assert added == Student("S002", "Grace Hopper", "grace@example.com")
    assert empty_manager.get_student("S002") is added


def test_student_manager_requires_name_and_email_for_id(empty_manager):
    with pytest.raises(ValueError, match="name and email must be provided"):
        empty_manager.add_student("S001")


def test_student_manager_rejects_invalid_add_student_argument(empty_manager):
    with pytest.raises(TypeError, match="Invalid argument"):
        empty_manager.add_student(123)


@pytest.mark.parametrize("add_as_instance", [False, True])
def test_student_manager_rejects_duplicate_student_id_without_overwriting(
    empty_manager, add_as_instance
):
    original = empty_manager.add_student("S001", "Ada Lovelace", "ada@example.com")
    duplicate = (
        Student("S001", "Different Student", "different@example.com")
        if add_as_instance
        else ("S001", "Different Student", "different@example.com")
    )

    with pytest.raises(ValueError, match="already exists"):
        if add_as_instance:
            empty_manager.add_student(duplicate)
        else:
            empty_manager.add_student(*duplicate)

    assert empty_manager.get_student("S001") is original
    assert empty_manager.get_total_students() == 1


def test_student_manager_get_student_raises_for_unknown_id(empty_manager):
    with pytest.raises(KeyError, match="not found"):
        empty_manager.get_student("missing")


def test_student_manager_updates_grade_and_returns_updated_gpa(empty_manager):
    empty_manager.add_student("S001", "Ada Lovelace", "ada@example.com")

    updated_gpa = empty_manager.update_grade("S001", "MATH101", 95)

    assert updated_gpa == 4.0
    assert empty_manager.calculate_gpa("S001") == 4.0


def test_student_manager_update_grade_raises_for_unknown_id(empty_manager):
    with pytest.raises(KeyError, match="not found"):
        empty_manager.update_grade("missing", "MATH101", 95)


def test_student_manager_removes_student_and_updates_count(empty_manager):
    empty_manager.add_student("S001", "Ada Lovelace", "ada@example.com")
    assert empty_manager.remove_student("S001") is True
    assert empty_manager.get_total_students() == 0
    with pytest.raises(KeyError, match="not found"):
        empty_manager.get_student("S001")


def test_student_manager_remove_unknown_student_raises_key_error(empty_manager):
    with pytest.raises(KeyError, match="not found"):
        empty_manager.remove_student("missing")


def test_populated_manager_ranks_students_and_respects_top_performer_limit(
    populated_manager,
):
    assert [
        student.student_id
        for student in populated_manager.get_top_performers(2)
    ] == ["S001", "S002"]
    assert [
        student.student_id for student in populated_manager.get_top_performers(1)
    ] == ["S001"]


def test_student_manager_top_performers_handles_result_boundaries(empty_manager):
    assert empty_manager.get_top_performers(3) == []

    empty_manager.add_student("S001", "Ada Lovelace", "ada@example.com")
    assert len(empty_manager.get_top_performers(3)) == 1

    for count in (0, -1):
        with pytest.raises(ValueError, match="positive"):
            empty_manager.get_top_performers(count)


def test_student_manager_top_performers_breaks_gpa_ties_by_name(empty_manager):
    zelda = empty_manager.add_student("S001", "Zelda", "zelda@example.com")
    amy = empty_manager.add_student("S002", "Amy", "amy@example.com")
    zelda.add_grade("COURSE", 90)
    amy.add_grade("COURSE", 90)

    assert empty_manager.get_top_performers(2) == [zelda, amy]


def test_populated_manager_filters_students_by_minimum_gpa(populated_manager):
    assert [
        student.student_id
        for student in populated_manager.filter_by_min_gpa(2.0)
    ] == ["S001", "S002"]
    assert [
        student.student_id for student in populated_manager.filter_by_min_gpa(4.0)
    ] == ["S001"]
    assert populated_manager.filter_by_min_gpa(0.0) == populated_manager.get_all_students()


@pytest.mark.parametrize("min_gpa", [-0.01, 4.01])
def test_student_manager_filter_rejects_minimum_gpa_outside_bounds(
    empty_manager, min_gpa
):
    with pytest.raises(ValueError, match="between 0.0 and 4.0"):
        empty_manager.filter_by_min_gpa(min_gpa)
