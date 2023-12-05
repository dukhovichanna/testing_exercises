import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url

@pytest.mark.parametrize(
        "str, expected",
        [
            pytest.param('https://github.com/dukhovichanna/testing_exercises/pull/1',True, id='return_true_for_pull_request_page_conversation_page'),
            pytest.param('https://github.com/dukhovichanna/testing_exercises/pull/1/files', False, id='return_false_forpull_request_page_files_page'),
            pytest.param('https://github.com/dukhovichanna/testing_exercises', False, id='return_false_on_non_pr_url')
        ]
)

def test__is_github_pull_request_url(str, expected):
    result = is_github_pull_request_url(str)

    assert result == expected