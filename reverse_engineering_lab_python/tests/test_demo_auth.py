import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from demo_auth import validate_credentials


class ValidateCredentialsTests(unittest.TestCase):
    def test_correct_credentials(self):
        self.assertTrue(validate_credentials("melisa", "blue-orbit-42"))

    def test_wrong_username(self):
        self.assertFalse(validate_credentials("someone", "blue-orbit-42"))

    def test_wrong_password(self):
        self.assertFalse(validate_credentials("melisa", "wrong-password"))

    def test_username_too_short(self):
        self.assertFalse(validate_credentials("ab", "blue-orbit-42"))

    def test_password_too_short(self):
        self.assertFalse(validate_credentials("melisa", "short"))


if __name__ == "__main__":
    unittest.main()
