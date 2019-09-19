# buy-coins-api
[![Build Status](https://travis-ci.com/dharmykoya/buy-coins-api.svg?branch=ch-project-readme)](https://travis-ci.com/dharmykoya/buy-coins-api)

This grapghql API returns the cost of buying and selling a bitcoin using the [coindesk API](https://api.coindesk.com/v1/bpi/currentprice.json)

## API documemation links

[Graphql API Documentation](https://buy-coin.herokuapp.com/)


## Installing

```sh
    $ git clone https://github.com/dharmykoya/buy-coins-api.git
    $ cd buy-coins-api
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    $ git checkout develop
```


## Running the application

Run the command below to run the application locally.
```sh
  $ python manage.py runserver
```


## Running the tests

Run the command below to run the tests for the application.
```sh
  $ pytest
```


## Built With

The project has been built with the following technologies so far:

* [Django](https://www.djangoproject.com/) - web framework for building websites using Python
* [GraphQL](https://graphql.org/) - query language for our APIs.
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python
* [Pytest](https://docs.pytest.org/) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
