# The Brief
## Introduction
One of NASA’s objectives is to inspire the next generation.

NASA also has a wealth of data that is already exposed to the public via its [Open API](https://api.nasa.gov/).

We’d like you to design/build an MVP educational website based on this Open API (and any other data that you would like to use) aimed at engaging children in the 11-16 age range.

We would love for you to suggest more concepts and ways of using the data, but one idea that we’d really like to try out is using images from the Mars Rover Photos feed. This provides a large number of images from all of the cameras on four NASA rovers that have landed on Mars, including the currently active Perseverance rover. We’d really like for your site to include a fun way of exploring these images.

Follow the instructions below to run the application locally and then integrate with NASA's Open API.

We can’t wait to see what you come up with!

# Requirements
The site should include:

* An engaging landing page to draw in users
* A way of exploring photos from the Mars rovers.
* Some ways of exploring data from the API or other information about NASA or Mars. This means using user input to make different API requests.

It is important that the site could be easily extended into a full project if the prototype is successful

# Getting Started

## First time setup

Install [Poetry](https://python-poetry.org/docs/) if you haven't already, and then run the command `poetry install` in a terminal, from this project folder. 

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup. You can do this from a terminal with this command:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This is where you should store any secrets (such as API Keys)

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Integrate with the API

Firstly, install the Requests library via Poetry by running the command `poetry add requests` in your terminal (from this folder). This will add it to your list of dependencies in the `pyproject.toml` file and also download it.

Your Python files in this project can now import and use the `requests` module. See [this quickstart documentation](https://docs.python-requests.org/en/latest/user/quickstart/) for how to use it.

You’ll need to get an API key by registering on the Open API website and then include it in your API requests, but you shouldn’t commit sensitive values like keys to source control. Instead, pass it to the code via an environment variable:
- Fill in your `.env` file with an API key variable. By convention, environment variable names are uppercase with underscores.
- You can access an environment variable from Python code by importing `os` and then using the expression `os.getenv('YOUR_ENV_VAR_NAME')`. 
