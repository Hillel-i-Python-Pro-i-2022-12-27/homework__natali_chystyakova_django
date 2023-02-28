**Hello everyone, my name is Natalie**
---
*Student Hillel IT School, I am from Dnipro.*
---
# :house:  Django
# Homework 8. Django. Templates. Data generators for users.
We give a list of user data:
1. Login
2. Email  phones
3. Password

# Homework 9. Django. Contacts and commands.
Make contacts
1. Name
2. Phone
3. Creation date (contact)
4. Date modified (contact)


# Homework 10. Django. Contacts and CRUD
Add contacts. Make CRUD for contacts:
1. View all contacts
2. Create contact
3. View contact
4. Edit Contact
5. Delete contact


# Homework 11. Django. Admin (with superuser for this)
1. Create a custom user model. Tie django to this model. You can even not redefine the fields.
2. Make command in makefile to create super user using createsuperuser
3. Create an admin panel for existing models.

# Homework 12. Django. Static, Media, Crispy Forms, CSS.
1. Add an SVG image (for example, as a logo) and a favicon to the site via static files.
2. Add CSS or SCSS via static files. Change some styles in the application.
3. Add upload media files. For example, uploading an avatar + displaying this avatar.
4. Connect crispy-forms + templates to the chosen framework. For example Bootstrap5.

# Homework 13. Django. Env, Postgres, Docker Compose profiles
1. Migrate some past django homework (using a database) from sqlite to postgres.
2. Implement getting settings through env-files and environment variables. 
3. database connection:
DEBUG
SECRET_KEY
ALLOWED_HOSTS

# Homework 14. Django. Session
1. Make a view using session storage. For example, store and display:
1.1 Datetime of last visit
1.2 Number of visits

Django. User (Sign up, Log in, Log out). Login required.
# Homework 15. Django. User (Sign up, Log in, Log out). Login required.
1. Add registration and authorization for the user.
2. Sign in and out of your account.
3. Add an avatar for the user (if not already done).
4. Restrict access to at least one page. At least so that only an authorized user can access it.


* :wrench: install and update requiremets before run projet: make init-dev
* :arrow_forward: run this project without docker: make homework-i-run
* :whale: run this project with docker: make d-homework-i-run
* :end: purge without docker: make homework-i-purge
* :anchor: purge with docker: make d-homework-i-purge


