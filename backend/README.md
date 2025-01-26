# CANotify Backend

This directory contains the backend built using Flask.

## Installation

Production builds are done using Docker and Docker Compose, though you can run the backend on its own as a docker container or as a development server. This makes it easy to move data processing to different servers when scaling the service or if using cloud providers is preferred.

To run the development server, first create a venv and install the dependencies (Python 3.10.5 required)

`python3 -m venv venv`

After activating your venv run

`pip install -e .`

The project is now installed for local development. Changes to the files under `backend/src` will be reflected in the installation without any work. Run the command again if you add new requirements for the package.

Note about packaging - all packages under `backend/src` are installed as python packages (so you can call `import api` for example). Seperate programs go under different packages. You should use absolute imports in these packages where possible (ex. `from database.models import User`) to avoid import issues. If the paths are too long for you,
use dot-relative imports like `from .models import User` from the database package. 

## Running

Run the development server using

`flask --app api.app run --debug`

This will open a development server with auto-reloading on changes to code, which should be exposed at `http://localhost:5000`. The `--app api.app` option uses the installed api package to find the Flask app to run.

## Use as API

Our fontend makes simple HTTP GET/POST requests to interact with the business logic of the system. The interface is REST-like and therefore integrates easily
with other tools. This would make it trivially easy to do analysis of data using pandas, machine learning, or other programs, and then return analysis to the backend
to be displayed to users

## Testing

After installing the required dependencies, all tests can be run by simply executing the command `pytest` in this folder.

Currently, we test most of our API calls with sample data, testing simple use cases and more complicated ones. Testing can be easily expanded in the future too, 
which will ensure the project can stand the test of time.
