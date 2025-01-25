# CANotify

CANotify is a way to allow people to collaboratively report common community to nationwide disasters or problems like fires, floods, or the spread of disease. Users can:
- Report a disaster (like a flood, earthquake, fire, or tsunami), which will be added to a database of user reports
- Subscribe to email or text notifications for reports made near them
- Use our API to make integrations with other tools and data analysis techniques

It's a expandable system that is built to last, incorporating extensive testing, docstrings, and good coding practices.

Our solution uses Flask for the backend and React to implement a frontend. It is designed
to be easily deployed using Docker and Docker Compose.

## Accessibility

The simple interface and lack of pop-ups or other distracting elements lets users focus on what's important and directs their eyes to the most important information first

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
   ```
   git clone git@github.com:Blindingtoast/oec-2025.git
   cd oec-2025
   ```

2. Build and run the application using Docker Compose:
   ```
   docker-compose up
   ```

3. Access the application at `http://localhost` (no port number needs to be specified, as NGINX is bound to port 80)


## Structure

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
