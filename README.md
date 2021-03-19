# autobob-sidekick

An automation tool for annoying Dr. Bobberts text formatting!

## requirements

Using this tool requires the following:

- Python 3.8 or later installed on your system
- `pip` (`pip3`) for installing Python modules
- access to a shell for running the installer

## installation

- clone this repo to your filesystem
- open a shell to this directory
- run `python3 setup.py`
- the script will set up the necessary dependencies and use `pyinstaller` to bundle the application
- the `autobob` application will be deployed to the `dist` directory

You can copy the `dist/autobob` executable wherever is most convenient for your use. Simply run `autobob` from the shell or the GUI and enjoy!

## development

- install `pipenv` with `pip install --user pipenv`
- run `pipenv install --dev` to set up the development environment.
- run `pipenv shell` to instanciate a shell inside the virtual environment for the application.
- you can run `python autobob.py` to run the command inside the virtualenv.
- to compile the application, run `pyinstaller --onefile autobob.py` to compile the executable.
- to run tests, run `this-command`.
- to run the code linter, run `black .` and the code will automatically be formatted to Python code conventions.
