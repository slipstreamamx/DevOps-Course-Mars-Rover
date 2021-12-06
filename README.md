# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

For local development a Github OAuth app needs to be setup and the CLIENT_ID and CLIENT_SECRET set in the `.env` file. Follow the Github [documentation](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/) on how to do this, with a callback URL as the homepage URL with a path of `login/callback`.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

NB this requires a mongodb connection string to have been set in your .env file. If you don't want to set up a mongodb instance to use then you can run the app with docker-compose which will create a local instance to use, see instructions in the docker section below.

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Vagrant

This project supports vagrant, a VM-based alternative to running development code locally. To install vagrant, follow the instructions [here](https://www.vagrantup.com/docs/installation). You will require an appropriate hypervisor - we recommend virtualbox.

To launch the VM, run `vagrant up` in the repository root. First-time setup will take a few minutes. Once complete, the production app will be available at [`http://localhost:5000/`](http://localhost:5000/).

### Docker

This project is configured to run in Docker, and contains separate build steps for local development and production images.

#### Local

```bash
$ docker build --target development --tag todo-app:dev .
$ docker run --env-file ./.env -p 5100:80 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app --name dev todo-app:dev
```

The app should then be running at http://0.0.0.0:5100/. The local development image mounts the app source code directly from the host, and will hot reload on changes without requiring a reload or rebuild. Do not use this image in production.

Alternatively, you can use docker compose to build and launch the local development image:

```bash
$ docker-compose up --build
```

#### Production

```bash
$ docker build --target production --tag todo-app:prod .
$ docker run -p 5100:80 todo-app:prod
```

The production environment must include the environment variables defined in `.env.template`. To test a production image locally, add the `--env-file ./.env` argument to `docker run`.

#### Debug

To run the container in debugging mode first launch the debug container:

```bash
$ docker-compose -f docker-compose-debug.yml up --detach --build
```

Next you'll want to make sure you have both the *Docker* & *Remote Development* extensions for VScode installed.

With these installed select the docker icon from the activity bar to find your container. Right click on it and select *Attach Visual Studio Code*:

![open container folder](./assets/attach_to_container.gif)

From here a new VSCode window should open. From here select the Explore from the activity bar (Ctrl/Cmd + E) which should now show a large button saying open folder. After clicking this button a drop down should appear where you can enter the app folder:

![open container folder](./assets/open_container_folder.gif)

Note you may need to install the Python extension inside the container to enable basic features like adding breakpoints.

From here you can debug the app as usual, selecting Run => Start Debugging => Flask and then enter the app name (`todo_app/app.py`).

#### Testing

The easiest way to run the unit tests is to execute pytest directly:

```bash
$ poetry run pytest tests
```

You can also use the test docker image:

```bash
$ docker build --target test --tag todo-app-test .
$ docker run --env-file ./.env.test todo-app-test tests
```

The easiest way to run the end-to-end tests is to use docker-compose:

```bash
docker-compose -f docker-compose-test.yml up --build --exit-code-from test
```

This will use a locally running instance of mongodb so requires no mongodb setup.

You can also run the end-to-end tests using pytest:

```bash
$ docker build --target test --tag todo-app-test .
$ docker run --env-file ./.env todo-app-test tests_e2e
```

 or by using the test docker image:

```bash
$ poetry run pytest tests_e2e
```

However this requires a mongodb connection string, which can be supplied via a `.env` file or set manually as the environment variable 
`MONGODB_CONNECTION_STRING`, so you need to setup a mongodb instance for the tests to use. The items collection in the default database
set by the connection string will be wiped before and after running the tests so make sure you don't use a database with data you'd like
to keep.

### Travis CI

We use Travis CI to automatically build and test the code. The config for this in .travis.yml. The build will run every time a pull request is opened or updated. The settings can be found here: https://travis-ci.com/github/CorndelWithSoftwire/DevOps-Course-Exercise/settings.

The build output can be found here: https://travis-ci.com/github/CorndelWithSoftwire/DevOps-Course-Exercise. It will also be linked to from each pull request.

Travis CI continuously deploys to Azure, by publishing production docker images to DockerHub, then calling the Azure WebApp CD callback, which causes the WebApp to pull the latest image from DockerHub.

You can view the live site [here](https://devops-todo-app.azurewebsites.net/).


### GitHub OAuth
You need to set up a Github OAuth App [here](https://github.com/settings/developers), and put the client ID and secret into environment variables.

The settings on GitHub require you to list a redirect URL to your app's callback route, so it is suggested to have a separate "App" for local and prod.

You can disable logins by setting the environment variable `LOGIN_DISABLED=True`, this is what the tests do.

If you are working locally, OAuth will complan about localhost being http instead of https, you can disable that by setting the environment variable `OAUTHLIB_INSECURE_TRANSPORT=1`.