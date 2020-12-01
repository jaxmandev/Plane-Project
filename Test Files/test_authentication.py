from authentication import Authentication
import unittest
import pytest


class TestAuthentication(unittest.TestCase):
    test_authen = Authentication("jake", "jake")

    def test_credential_manager(self):
        # Checking the result when a  user is found in the database
        self.assertNotEqual(self.test_authen.credential_manager("jake"), False)
        # Checking the result when a user is not found
        self.assertFalse(self.test_authen.credential_manager("barrybluejeans"))

    def test_check_login(self):
        # Checking the result when the login credentials are correct for an admin
        self.assertEqual(self.test_authen.check_login("dev", "dev"), "admin")
        # Checking the result when the login credentials are correct for a user
        self.assertEqual(self.test_authen.check_login("jamie", "jamie"), "user")
        # Checking the result when the login credentials are incorrect
        self.assertRaises(Exception, self.test_authen.check_login("jake", "notjake"))

    def test_db_credentials(self):
        # Checking if an exception is raised when the user can't log in with the provided details
        with self.assertRaises(Exception):
            self.test_authen.db_credentials(False)
        # Checking if
        checking_admin_tuple = ("jake", "user")
        self.assertTupleEqual(
            checking_admin_tuple, self.test_authen.db_credentials("user")
        )

    # Needs sample user added rather than changing Jake

    # def test_password(self):
    #     # Checking the result when a username can not be found in the database
    #     self.assertFalse(self.test_authen.password("barrybluejeans", "barryspassword"))
    #     # Checking the result of changing a password for a username that can be found in the database
    #     self.assertTrue(self.test_authen.password("jake", "newjake"))
    #     # Checking if you can log in with the new password
    #     self.assertNotEqual(self.test_authen.check_login("jake", "newjake"), False)
