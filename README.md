# Flask Application Readme
This is a Flask application that allows users to log in and register their email address. Registered users can view the list of all registered users and delete their own user record from the database.

# Preview Application Live:
**Link: http://sallufullstack.pythonanywhere.com/**

# Requirements
-Python 3.6 or higher
-Flask
-Flask SQLAlchemy
-MarkupSafe

# Installation and Setup
1. Clone or download the repository.
2. Open a terminal and navigate to the directory where the repository is cloned or downloaded.
3. Create a virtual environment using the following command:

**python -m venv venv**

4. Activate the virtual environment:

(On Bash) **source venv/bin/activate**

(On Windows) **venv\Scripts\activate**

5. Install the required packages:

   **pip install -r requirements.txt**

6. Start the application:

**python app.py**

# Usage
Once the application is running, open a web browser and go to http://localhost:5000/ to access the login page.

# Login
On the login page, enter your name and gender and click on the login button. This will create a new user if it does not already exist in the database or update the user's gender if it does exist. If the user's email address is already registered, it will be retrieved from the database and stored in the user's session.

# User Profile
After logging in, the user is redirected to their profile page, where they can view and edit their email address. Any changes made to the email address will be stored in the database.

#View All Users
To view the list of all registered users, click on the "View All Users" button on the navigation bar. This will display a table with the name and email address of all registered users.

# Delete User
To delete a user, click on the "Delete User" button on the navigation bar. This will delete the user's record from the database and log the user out. If the user has an email address registered in the database, it will also be deleted.

# Logout
To log out, click on the "Logout" button on the navigation bar. This will clear the user's session and redirect them to the login page.

# License
This application is licensed under the MIT License. See LICENSE for more information.
