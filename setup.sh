#!/usr/bin/env bash

echo "Running AutoBob SideKick Setup..."

if [[ ! "$(python3 -V)" =~ "Python 3" ]]; then
    echo "Error: Python 3 is not installed!"
    exit 1
fi

if [[ ! "$(pip3 --version)" =~ "python 3" ]] || [[ ! "$(pip --version)" =~ "python 3" ]]; then
    echo "Error: No compatible version of pip installed!"
    exit 1
fi

if [[ ! "$(pipenv --version)" =~ "pipenv" ]]; then
    echo "Installing pipenv..."
    pip install pipenv
    if [[ $? != 0 ]]; then
        pip3 install pipenv
        if [[ $? != 0 ]]; then
            echo "Error: failed to install pipenv!"
            exit 1
        fi
    fi
fi

echo "Setting up virtual environment..."
pipenv install
if [[ $? != 0 ]]; then
    echo "Error: failed to set up virtual environment!"
    exit 1
fi

echo "Compiling executable..."
pipenv run pyinstaller --noconsole --onefile autobob.py
if [[ $? != 0 ]]; then
    echo "Error: failed compile application!"
    exit 1
fi

cp ./dist/autobob .
echo "AutoBob SideKick has been compiled successfully!"
echo "On Linux, copy the 'autobob' exe to your ~/bin directory."
echo "On Mac, copy the 'autobob' exe to your /Applications directory."
echo "On Windows, copy the 'autobob' exe to wherever you're gonna run it from."

exit 0