# OEC

Our solution for OEC uses uses Flask for the backend and React to implement a frontend. It is designed
to be easily deployed using Docker and Docker Compose.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
   ```
   git clone <repository-url>
   cd oecdesign
   ```

2. Build and run the application using Docker Compose:
   ```
   docker-compose up
   ```

3. Access the application at `http://localhost` (no port number needs to be specified, as NGINX is bound to port 80)


## Overview

This application is split into a backend and frontend component. They interact with eachother through HTTP GET/POST requests.

NGINX acts as a reverse proxy and serves the static assets. This makes it possible to expand in the future to cloud computing services
or to deploy to a variety of different servers. This gives our solution scalability and makes it much more robust than just being a
simple application.

## The Team

Our names are Angus Jull, Aashna Verma, Brian Tran, and Noah Gagnon. Our team name is AJR.

## Reading the Code

Check out the README.md files in the frontend and backend to learn a little more about our project. Then read through some of our source material
to get to know it better. As is standard practice, our code is self-documenting and comments are only included where it is necessary to reduce
unnecessary duplication of information.

## Citations

We use a number of Python and NPM packages, which can be seen in the requirements.txt and package.json files. We also use Docker to run our solution and NGINX to serve our solution.
