from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase
from cards.forms import EmailUserCreationForm
from cards.models import Player


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Player  is M4 so that this username we're testing is already taken
        Player.objects.create_user(username='M4')

        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'M4'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username_pass(self):
        Player.objects.create_user(username='juji')
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'unique'}
        form.clean_username()

    def test_register_sends_email(self):
        form = EmailUserCreationForm()
        form.cleaned_data = {
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'test-pw',
            'password2': 'test-pw',
        }
        form.save()
        # Check there is an email to send
        self.assertEqual(len(mail.outbox), 1)
        # Check the subject is what we expect
        self.assertEqual(mail.outbox[0].subject, 'Welcome!')
