# Contact-Log CLI

A command-line application for managing professional and personal contacts and logging communication history.

## Features
- Create, view, update, and delete contacts
- Log communications (date, notes) for any contact
- Search contacts by name
- Filter communications by date range
- View related objects (all communications for a contact)

## Installation
1. Clone the repository
2. Run `pipenv install`
3. Activate the environment with `pipenv shell`

## Usage
Run `python lib/cli.py` to start the application.

## File Structure
contact-log-cli/
├── Pipfile
├── README.md
└── lib/
├── cli.py # Main CLI interface
├── debug.py # Testing script
├── database.py # Database connection setup
├── helpers.py # Helper functions
└── models/
├── init.py
├── contact.py # Contact model
└── communication.py # Communication model
