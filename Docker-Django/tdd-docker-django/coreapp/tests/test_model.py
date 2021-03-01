from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTestCase(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a new user with email is successful"""
        email = 'vivek@gmail.com'
        password = "test@1234"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalization(self):
        """ test email for new user is normalise """
        email = 'vivek@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test@1234')
        self.assertEqual(user.email,email.lower())



    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises erroe """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test@1234')

    
    def test_create_new_superUser(self):
        """ test for create new superuser """

        user = get_user_model().objects.create_superuser(
            'vivek@gmail.com',
            'test@1234'
        )
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
