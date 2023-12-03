from functions.level_2.one_pr_url import is_github_pull_request_url

def test__is_github_pull_request_url__pull_request_page_conversation_page():
    url = 'https://github.com/dukhovichanna/testing_exercises/pull/1'
    assert is_github_pull_request_url(url) == True

def test__is_github_pull_request_url__pull_request_page_non_conversation_page():
    url = 'https://github.com/dukhovichanna/testing_exercises/pull/1/files'
    assert is_github_pull_request_url(url) == False

def test__is_github_pull_request_url__non_pull_request_url():
    url = 'https://github.com/dukhovichanna/testing_exercises'
    assert is_github_pull_request_url(url) == False