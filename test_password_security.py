import Password_Security

def test_verify_password_correct():
    hashed = Password_Security.hash_password("Godisgood1")
    assert Password_Security.verify_password(hashed, "Godisgood1")
def test_verify_password_incorrect():
    hashed = Password_Security.hash_password("Godisgood1")
    assert not Password_Security.verify_password(hashed, "incorrectpassword")
