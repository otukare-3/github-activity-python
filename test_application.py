import pytest

from github_activity import get_github_activity


def test_valid_user():
    user_name = "otukare-3"
    result: list[any] = get_github_activity(user_name)
    assert result.pop() is not None

def test_invalid_user():
    user_name = "foo_foo_foo_foo_foo_foo"
    with pytest.raises(Exception) as e:
        get_github_activity(user_name)
    assert e is not None

