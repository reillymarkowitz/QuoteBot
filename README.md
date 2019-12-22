# Getting started

QuoteBot is a simple Python Twitter bot that periodically tweets quotes from a given author.
Sample implementation here: https://twitter.com/AntiOedipusBot

## Clone this repository

### Using SSH

    git clone git@github.com:reillymarkowitz/twitter-book-bot.git

### Using HTTPS

    git clone https://github.com/reillymarkowitz/twitter-book-bot.git

## Create a virtual environment

It's recommended that you create a virtual environment after cloning the repo. This can be done using virtualenv on Linux:

    pip install virtualenv

Test your installation:

    virtualenv --version

Create a new virtualenv using a copy of Python 3:

    cd twitter-book-bot
	virtualenv -p /path/to/python3 venv

Activate the new virtualenv:

    source venv/bin/activate

When you're done working in the virtual environment, deactivate it:

    deactivate

## Install dependencies

Install the required dependencies with `pip`:

    pip install -r requirements.txt

## Set environment variables

For the bot to work with your Twitter account, you must create a `.env` file in the project root directory containing your account's access credentials:

    # twitter-book-bot/.env contents
    CONSUMER_KEY=[YOUR CONSUMER KEY]
    CONSUMER_SECRET=[YOUR CONSUMER SECRET]
    ACCESS_TOKEN=[YOUR ACCESS TOKEN]
    ACCESS_TOKEN_SECRET=[YOUR ACCESS TOKEN SECRET]

If you don't have these credentials, create a new Twitter app [here](https://developer.twitter.com/en/apps).
