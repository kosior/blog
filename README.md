# Blog

[![Build Status](https://travis-ci.com/kosior/blog.svg?branch=master)](https://travis-ci.com/kosior/blog) [![codecov](https://codecov.io/gh/kosior/blog/branch/master/graph/badge.svg)](https://codecov.io/gh/kosior/blog)

Simple blog created with Python and Django.

This blog reqiures Python 3.4+.

## Setting up a development environment

Clone the repository:

    git clone https://github.com/kosior/blog.git

Step into newly created `blog` directory:

    cd blog

It's recomended to create a new virtual environment. Then, install all the required dependencies:

    pip install -r requirements.txt
    
Run the migration to create database schema:

    python manage.py migrate
    
Run your local server:

     python manage.py runserver

## Tests

To run the tests:
    
    python manage.py test
    
To generate coverage run:

    coverage run manage.py test
    
For a coverage report run:

    coverage report
