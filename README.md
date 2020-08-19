
This is a simple Python Django time management system that allows users create an account and log in, add (and edit and delete) a row what they have worked on, what date, for how long. This system has three roles with different permission levels: a regular user would only be able to CRUD on their owned records, a user manager would be able to CRUD users, and an admin would be able to CRUD all records and users. The system includes a REST API that makes it possible to perform all user actions via the API, including authentication and implements AJAX for better user experience.


Features
========

- Built with Python 3.6, Djang0 2.0 Framework
- Styled using Bootstrap4
- Uses PostgreSQL DB and Deployed to Heroku
Allows users to:
- Sign in with the application to start using.
- add (and edit and delete) a row what he has worked on, what date, for how long.
- Set up a profile about me and be able to update profile as needed.
- Perform all user actions via the REST API, including authentication
- Search Postings based on Post title
- Create Posts that will be visible to everyone 
- Perform CRUD operations on posts they own




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to:

-   Have python installed
-   Have PostgreSQL DB installed
-   Have a terminal to interact with the app.
-   Any text editor
-   Browser to view
-  -Create a Virtual Environemnt, install Django >=2.0 and its dependencies


Installation
========

    $ git@github.com:jameskomo/time-management-system.git


Build & Deployment
========

**NOTE:** You need to have fully cloned it to run it locally.


    (virtual) $ python3.6 manage.py runserver

    # it will launch the web page from local server. You can also visit the livelink [here](https://softsearch.herokuapp.com/).
 to use the system

##Built With

- Built with Python 3.6
- Django2.0
- Styled using Bootstrap

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

Known Bugs
========
There are currently no known bugs for the app. However, I will be updating the README incase any bugs arise.
