#Developer- Anand Sagar Rout
#Project Name- contact management system
#File- test_contacts.py

import unittest
from unittest.mock import patch
from contact_manager import validate_phone, validate_email, add_contact, delete_contact

class TestValidatePhone(unittest.TestCase):

    def test_valid(self):
        valid, digits = validate_phone("9876543210")
        self.assertTrue(valid)

    def test_invalid_short(self):
        valid, _ = validate_phone("12345")
        self.assertFalse(valid)


class TestValidateEmail(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(validate_email("anand@gmail.com"))

    def test_invalid(self):
        self.assertFalse(validate_email("anandgmail.com"))


class TestAddContact(unittest.TestCase):

    def setUp(self):
        self.contacts = {}

    @patch('builtins.input', side_effect=["Anand Yadav", "9876543210", "", "", ""])
    def test_add_valid(self, mock):
        add_contact(self.contacts)
        self.assertIn("Anand Yadav", self.contacts)

    @patch('builtins.input', side_effect=["", "", "", "", ""])
    def test_add_empty_name(self, mock):
        add_contact(self.contacts)
        self.assertEqual(len(self.contacts), 0)

    @patch('builtins.input', side_effect=["Anand Yadav", "123", "", "", ""])
    def test_add_invalid_phone(self, mock):
        add_contact(self.contacts)
        self.assertNotIn("Anand Yadav", self.contacts)


class TestDeleteContact(unittest.TestCase):

    def setUp(self):
        self.contacts = {
            "Anand Yadav": {"Phone": "9876543210", "Email": "", "group": "Home", "address": "", "Created at": "", "Updated at": ""}
        }

    @patch('builtins.input', side_effect=["Anand Yadav", "y"])
    def test_delete(self, mock):
        delete_contact(self.contacts)
        self.assertNotIn("Anand Yadav", self.contacts)

    @patch('builtins.input', side_effect=["Anand Yadav", "n"])
    def test_delete_cancelled(self, mock):
        delete_contact(self.contacts)
        self.assertIn("Anand Yadav", self.contacts)


# ================= MAIN ================= #

if __name__ == "__main__":
    unittest.main()