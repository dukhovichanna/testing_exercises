import os
from functions.level_4.four_lines_counter import count_lines_in

def test__count_lines_in__do_count_return_true_when_3_lines_of_code_and_ignore_one_comment(temp_file_with_content):
    file_path = temp_file_with_content
    result = count_lines_in(file_path)
    assert result == 3


def test__count_lines_in__return_none_when_nonexistent_file_path():
    file_path = "nonexistent_file.txt"
    result = count_lines_in(file_path)
    assert result is None


def test_count_lines_in__do_return_true_when_file_contains_only_comments(temp_file_with_content):
    file_path = temp_file_with_content
    with open(file_path, "w") as file:
        file.write("# Comment 1\n# Comment 2")
    result = count_lines_in(file_path)
    assert result == 0