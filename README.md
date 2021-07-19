# Django Web Framework and TheMovieDatabase API
## Description
I accepted the friendly challenge from [B2BLUE](https://www.b2blue.com) to build a micro-project in django framework that integrates the API of [TheMovieDatabase](https://www.themoviedb.org/) , as a demonstration of my skills using the tools of Django, Docker, Git and general knowledge in software development.
## Table of Contents (Optional)
If your README is long, add a table of contents to make it easy for users to find what they need.
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [License](#license)
## Installation
- `git clone https://github.com/danieltorrescode/themoviedb.git`
- `cd themoviedb`
- If just running with docker : `docker-compose up`
- `pip -r requirements.txt`
- `cd themoviedb/django`
- `python manage.py runserver`

it is recomended the use of [virtualenv](https://pypi.org/project/virtualenv/)
- `pip install virtualenv`
- `python virtualenv -p 3.x.x venv`
- `cd venv`
- `source bin/activate`
## Features
This is a Django application that integrates with TheMovieDatabase API's
and display the most popular TV series, displaying information in the
application such as name, description, year of release,
poster image of the show. Within the application it will be possible to
filter by name, year of release and popularity of the series.
## Tests
Django provides a small set of tools using a Python standard library module: unittest for writing tests.
- `cd themoviedb/django`
- `python manage.py test`

## License
GPLv3+