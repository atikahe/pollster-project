# Pollster-project
This is a polling project built entirely on Django framework.

## Usage
1. Create virtual environment
```bash
pip shell
```
2. Make migrations
```bash
python manage.py makemigrations pollster
python manage.py migrate        // this will migrate all boilerplate table as well as apps table
```
3. Insert data to db from shell
4. Create superuser
```bash
python manage.py createsuperuser
```
Add ```winpty``` before ```python``` if command fails.
Then, register your email and password.

5. Run server and access app at 8080
```bash
python manage.py runserver 8080
```
6. From browser, access '/admin' url, and login using previously created super user account.
7. From browser, access '/polls/ url to see polling page.

## To Do
- [x] Project Setup
- [x] Admin page feature
- [x] View polling question
- [x] View polling result
- [ ] Voting feature (built, not yet working)
- [ ] Unit test setup
- [ ] Deployment

## Resources
- [Django](https://www.djangoproject.com/start/)
- [SQLite3](https://www.sqlite.org)
