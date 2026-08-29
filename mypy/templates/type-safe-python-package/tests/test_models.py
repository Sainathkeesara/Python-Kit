from type_safe_pkg.models import User, get_user_greeting


def test_user_greeting():
    user = User(id=1, name="Alice", email="alice@example.com")
    assert get_user_greeting(user) == "Hello, Alice!"
