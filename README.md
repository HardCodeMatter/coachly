# eCoachly

![Logo](https://imgur.com/7rfCklq.png)

eCoachly is an online platform for creating, joining and performing course tasks. Project is developed for educational purposes.
## Tech Stack

* `Python`
* `Django`
* `SQLite`
* `Bootstrap5`
* `django-crispy-forms`


## Features

- Built-in authentication and authorization
- Responsive template
- Users:
    - Authenticated users can:
        - `sign up`;
        - `log in`;
        - `log out`;
        - `create` course;
        - `join` course;
- Courses:
    - Courses have members with roles: 
        - teachers;
        - students;
    - Teachers can:
        - `edit` course info;
        - `add` / `edit` / `delete` announcements;
        - `create` / `edit` / `delete` tasks;
        - `view` members;
        - `grade` students;
    - Students can:
        - `add` / `delete (own)` announcements;
        - `view` tasks;
        - `view` members;
        - `view` grades;
    - There is a blue star next to the course author's name;
    - Course may have a premium status;
## Screenshots

* `Course list`
![App Screenshot](https://imgur.com/ruDFvnJ.jpg)

* `Course main page`
![App Screenshot](https://imgur.com/hrEwQNL.jpg)

* `Course grades page`
![App Screenshot](https://imgur.com/RPjyFNO.jpg)

* `Course members page`
![App Screenshot](https://imgur.com/9mUhPHV.jpg)
## Installation

Install eCoachly project by bash from GitHub repository.

```bash
 mkdir coachly && cd coachly
 git clone https://github.com/hardline-dev/coachly.git
```

To start local server, use following command:
```bash
 python3 manage.py runserver
```

To perform database migrations, use following command:
```bash
 python3 manage.py makemigrations
 python3 manage.py migrate
```
