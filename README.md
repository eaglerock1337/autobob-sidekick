# autobob-sidekick

An automation tool for annoying Dr. Bobberts text formatting!

## requirements

Using this tool requires the following:

- Python 3.6 or later installed on your system
- `pip` (`pip3`) for installing Python modules
- access to a shell for using the makefile or installer

## installation

- clone this repo to your filesystem
- open a shell to this directory
- run `make` if you have it installed, otherwise run `setup.sh`
- the makefile/script will set up the necessary dependencies and use `pyinstaller` to bundle the application
- the `autobob` application will be copied to the current directory

You can copy the `autobob` executable wherever is most convenient for your use. Simply run `autobob` from the shell or the GUI and enjoy!

## development

- install `pipenv` with `pip install --user pipenv`
- run `pipenv install --dev` to set up the development environment.
- run `pipenv shell` to instanciate a shell inside the virtual environment for the application.
- you can run `python autobob.py` to run the command inside the virtualenv.
- you can alternatively run `pipenv run python autobob.py` outside of the virtualenv.
- to compile the application, run `make compile` to compile the executable.
- to specify an icon, add `--icon /path/to/icon/file` to the `pyinstaller` command.
- to run tests, run `make test`.
- to run the code linter, run `black .` and the code will automatically be formatted to Python code conventions.
- to test `pyinstaller`, `make`, or `setup.sh` in a container, use `make docker` to set up a docker container.

## program layout

The following files make up the application and its data:

- `autobob.py` - Main program that uses the `sidekick` module
- `Makefile` - Make tools for running and compiling the application
- `setup.sh` - A setup script for systems without `make` installed
- `sidekick/autobob.py` - `AutoBob()` class and its member functions
- `sidekick/codes.py` - Lists and dicts for treatment and auxillary codes
- `sidekick/fields.py` - Fields and output text for specific fields
- `sidekick/layouts.py` - Layout nested lists for PySimpleGUI window formatting
- `Dockerfile` - A Docker image for testing the `pyinstaller` and setup commands

The other files and directories are as follows:

- `dist/` - Generated by `pyinstaller` for outputting `dist/autobob` executable
- `.gitignore` - Used by git to know which files to ignore in source control
- `autobob.spec` - Generated by `pyinstaller` when creating executable file
- `LICENSE` - BSD 3-Clause license for sharing to others
- `NOTES.md` - Notes taken for how program should work
- `Pipfile` - Used by `pipenv` to define the program's virtual environment
- `Pipfile.lock` - Used by `pipenv` when generating the virtual environment locally
