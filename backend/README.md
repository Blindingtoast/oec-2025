# Backend

This directory contains the backend built using Flask.

## Installation

Production builds are done using Docker and Docker Compose, though you can run the backend on its own as a docker container or as a development server. This makes it easy to move data processing to different servers when scaling the service or if using cloud providers is preferred.

To run the development server, first create a venv and install the dependencies (Python 3.10.5 required)

`python3 -m venv venv`

After activating your venv run

`pip install -r requirements.txt`

The project is now installed for local development

## Running

Run the development server using

`python3 app.py`

This will open a development server with auto-reloading on changes to code, which should be exposed at `http://localhost:5000`

## Use as API

Our fontend makes simple HTTP GET/POST requests to interact with the business logic of the system. The interface is REST-like and therefore integrates easily
with other tools. This would make it trivially easy to do analysis of data using pandas, machine learning, or other programs, and then return analysis to the backend
to be displayed to users

To view API calls, you can check out the ./api directory, where our calls are defined in Flask, using Pydantic models to validate data on entry and exit. This adds robustness to the design and ensures easy integration

## Components

The backend has been broken up into a few major components

```
backend
├── api       # Contains the code for data processing and other application logic
├── database  # Contains code for interactive with persistent storage
├── functions # Contains the logic for notifying users (and interaction with twilio, which provides the notification service)
├── database  # Contains code for interactive with persistent storage
├── tests     # Contains code for testing (see [Testing](#testing) for how to test)
└── app.py    # Creates the Flask app (see [Running](#running) for how to run)
```

This is to allow for future expansion and make it easy to encourage good coding practice, like minimizing coupling.
They also make it easy to find where important logic is for future maintainers.


## Testing

After installing the required dependencies, all tests can be run by simply executing the command `pytest` in this folder.
Good testing is a core part of good software, and luckily Flask allows for complete coverage of application code.

Currently, we test most of our API calls with sample data, testing simple use cases and more complicated ones. Testing can be easily expanded in the future too, 
which will ensure the project can stand the test of time.
