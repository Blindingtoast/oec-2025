# Backend Flask Application

This directory contains the backend of the fullstack application built using Flask.

## Installation

Production builds are done using Docker and Docker Compose (see the readme a folder up)

To run the development server, first create a venv and install the dependencies (Python 3.10.5 required)

`python3 -m venv venv`

After activating your venv run

`pip install -r requirements.txt`

The project is now installed for local development

## Running

Run the development server using

`flask dev api/main.py --debug`

This will open a development server with auto-reloading on changes to code, which should be exposed at `http://localhost:5000`

## Components

The backend has been broken up into a few major components

```
backend
├── api      # Contains the code for data processing and other application logic
├── database # Contains code for interactive with persistent storage
├── tests    # Contains code for testing (see [Testing](#testing) for how to test)
└── app.py   # Creates the Flask app (see [Running](#running) for how to run)
```

This is to allow for future expansion and make it easy to encourage good coding practice, like minimizing coupling.
They also make it easy to find where important logic is for future maintainers.


## Testing

After installing the required dependencies, all tests can be run by simply executing the command `pytest` in this folder.
Good testing is a core part of good software, and luckily Flask allows for complete coverage of application code.
