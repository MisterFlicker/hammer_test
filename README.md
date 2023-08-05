hammer_test - is Imitation of the referral system.

Authorization by phone number.

Assigning each phone number its own invite code.

The ability to see a list of users who entered your invite code.

Ability to enter someone else's invite code yourself.

## How to install

### Dependencies:

- Python >= 3.8
- Django >= 4.2.3
- psycopg2-binary >= 2.9.6
- gunicorn >= 21.2.0
- dj-database-url (for working remote database) >= 2.0.0

### Installing

Type in terminal:

1) make install
2) make build

## How to use

Type in terminal:
- For starting with gunicorn: make start
- For starting with manage.py: make run

## API description (deployed on render.com)
- **GET** *hammer-test.onrender.com/* - get page with start authorization button.
___
- **GET** *hammer-test.onrender.com/authorization* - get page with form to enter a phone number and submit button.

**Options**:
1) django form of phone.
___
- **GET** *hammer-test.onrender.com/authorization/* - after 2 sec delayed (imitation of creation 4-symbol code) get page with phone form and authorization code form (can type any 4 symbols). This request checking phone in database and loading GET form if phone already in database or POST form for new phone.

**Options**:
1) django form of phone;
2) number of phone and status of phone in database (exists or not).
___
- **POST** *hammer-test.onrender.com/user/phone* - after authorization of an new user get new user profile page with user's invite code, invite code form, and empty list of other user's phones (who activated our invite-code).

**Options**:
1) django form of invite code;
2) number of phone;
3) empty value of entered invite code;
4) own invite code;
5) empty list of other phones.
___
- **POST** *hammer-test.onrender.com/user/phone* - after entering invite-code get user profile page similar to the previous, but list of phones can be not empty. 3 variants of this page:
1) If entered invite-code is correct. Form will never be displayed on page for this user. Instead the entered invite code will be displayed.
2) If entered invite-code is own user's code. A message will be displayed next to the form about the impossibility to enter your own invite code.
3) If entered invite-code does not exist. A message will be displayed next to the form about not existed code.

**Options**:
1) django form of invite code;
2) number of phone;
3) empty value of entered invite code (if code does not exist or it's own code). Entered code value if code is correct.
4) own invite code;
5) list of other phones, who entered your own invite code.
___
- **GET** *hammer-test.onrender.com/user/phone* - after authorization of an existing user get page with user's invite code, entered invite-code (or empty form for entering code - if user didn't enter code before), list of other phones.

**Options**:
1) django form of invite code;
2) number of phone;
3) empty value of entered invite code (if code wasn't entered). Entered code value if code was entered.
4) own invite code;
5) list of other phones, who entered your own invite code.


