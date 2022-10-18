# Family Star Back-End
## Table of contents
- [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and libraries](#frameworks-and-libraries)
	- [Databases](#databases)
	- [Storage](#storage)
    - [Other tools](#other-tools)
- [Database Scheme](#database-scheme)
- [Testing](#testing)
- [Future improvements](#future-improvements)
    - [Code](#code)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Code](#code)
    - [Typography](#Typography)
	- [Icons](#icons)
	- [Wireframes](#wireframes)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
    - [Code](#code)
- [Test](#test)

## Technologies used
### Languages
- [Python (3.8.11)](https://www.python.org/)
### Frameworks and libraries
- [Django (3.2.15) ](https://www.djangoproject.com/) - Used for core functionality 
- [Django rest framework (3.13.1)](https://www.django-rest-framework.org/)
- [Django rest auth (2.2.5)](https://django-rest-auth.readthedocs.io/en/latest/) - Used for authentication and registration
- [Django cors headers (3.13.0)](https://pypi.org/project/django-cors-headers/) - Used for allowing Cross-Origin Resource Sharing
- [Pytest (7.1.2)](https://pypi.org/project/pytest/) and [Pytest-django (4.5.2)](https://pytest-django.readthedocs.io/en/latest/) - Used for testing Python
### Databases
- [SQLite](https://www.sqlite.org/index.html) - Used as development database 
- [PostgreSQL](https://www.postgresql.org/) - Used as production database
### Storage
- [Cloudinary](https://cloudinary.com/) - Used for storing pictures
### Other tools
- [GitHub Issues](https://github.com/features/issues) - Used for project planning 
- [Gunicorn (20.1.0)](https://gunicorn.org/) - Used as inspiration when maping out categories 
- [Graphviz](https://dreampuf.github.io/GraphvizOnline/) - Used for generating pretty database schema from dot-file
- [Heroku](https://id.heroku.com/login) - Used to deploy app
- [Pyscopg2 (2.9.3)](https://pypi.org/project/psycopg2/) - Used for connecting PostgreSQL to Python 
### Database Scheme
<img src="documentation/readme-images/db_scheme.svg">

## Testing
Read more about test and validation [here](/testing/TEST.md)

## Future improvements
### Code
- To do maintainability easier the search and filter functionality could be moved to it's own method.
## Deployment
## Credits
### Code
- [Django REST framework documentation](https://www.django-rest-framework.org/) - Used throughout the project.
- [Stackoverflow - Q](https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering) - Used as inspiration when creating functionality for filtering and searching tasks
- [Stackoverflow - Write explicit update](https://stackoverflow.com/questions/62847000/write-an-explicit-update-method-for-serializer) - Used as inspiration when updating task
- [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/) - Used as inspiration when creating Django signals.

### Test
- [Pytest-django Documentation](https://pytest-django.readthedocs.io/en/latest/) - Used as guide when writing tests
- [Django REST framework](https://www.django-rest-framework.org/api-guide/testing/) - Used as guidie when writing view tests
- [Stackoverflow - bytes type to dictionary](https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary) - Used hwne writing view test 