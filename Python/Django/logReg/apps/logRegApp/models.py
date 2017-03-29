from __future__ import unicode_literals

from django.db import models
import bcrypt
from bcrypt import hashpw, gensalt
# Create your models here.

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        # print data-----the print data and the return True are for testing that data is being collected and sent somewhere. these are not needed for the validation.

        # return True
        #the above steps are run after the r_process in the views.py file runs and sends the information in the result=User.objects.validate(data) line. The print data line will print out the entered information in the terminal and then return a value of True. This will then go back to the views.py file and run the print result, which will be True because the result was set to True and continue with the next command in the r_process funciton.
        flag = True
        errors = []
        # ^^^^^this keeps a list of errors in the validation process so that they can be called later as flash messages to display what the user did not enter or did not eneter correctly.
        password=data['pass']
        hashed = bcrypt.hashpw(str(password),bcrypt.gensalt())
        #^^^^^ this is for encrypting the passwrod that the user submits.
        print hashed
        print'!@$%&'*27
        #this is the validation for the registration information in the index.html page.
        if len(data['first_name']) < 2:
            flag = False
            errors.append("First name must be at least two characters long.")
            #this adds an error message into the errors list that was created under the flag = True statement.
        if len(data['last_name']) < 2:
            flag = False
            errors.append("Last name must be at least two characters long.")

        if not EMAIL_REGEX.match(data['email']):
            flag=False
            errors.append("You did not entere a valid email")
            # the EMAIL_REGEX will check and make sure that the email contains letter/numbers, an @, leters/numbers, a . and leters

        if data['pass'] != data['cpass']:
            flag = False
            errors.append('Passwords must match')

        if len(data['pass']) < 8:
            flag = False
            errors.append("Password must be at least 8 characters long")

        if flag:
            #if the flag is still true

            user=User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['pass'])

            # this will add the data from the input fields into the database if the flag remains True, meaning that none of the above if statements set the flag to False. That would happen if any of the checks return True,i.e. the first name is less than 2 characters long, the flag is set to False, erros messages are dispalyed and nothing is created in the database.
            return (True, user)
        else:
            return (False, errors)#if the flag is False, False will be returned and the list of errors will be sent to the views.py file. The tuples that are being returned, (True, user) and (False, errors) will be used by the views.py file to do the next step. See STEP after result=User.objects.validate(data)


    def l_process(self,data):
        flag = True
        errors = []
        suspect_user = User.objects.filter(email=data['email'])
        if not suspect_user:
            flag = False
            errors.append('Invalid email')
            return (False, errors)
            #check password this is where bcrypt will be placed to cheeck the password has against the password input on the login portion of the index.html page.
            hashed = suspect_user[0].password
            password = str(data['pass'])
            if bcrypt.hashpw(password, hashed) == hashed:
                print hashed
                print"*"*35
                print password
                return (True, User.objects.filter())



            else:
                flag = False
                errors.append("Invalid password")
            return (False, errors)

        # if suspect_user[0].password != data['pass']:
        #     flag = False
        #     errors.append("Invalid Password!")
        #     return (False, errors)
            # in the above if statement, if the password enetered in the text field does not match the suspect_user that we got from the email entered, the flag will be set to false and an error message will be put into errors. Make sure to include the return so that the error message will display. otherwise the application will throw an error like object has no attribute.
        else:
            return (True, suspect_user[0])
        # else:
        #     flag = False
        #     errors.append("Invalid Email!")

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
