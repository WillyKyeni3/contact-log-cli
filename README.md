# Contact-Log CLI

A command-line application for managing professional and personal contacts and logging communication history.

## Features
- Create, view, update, and delete contacts
- Log communications (date, notes) for any contact
- Search contacts by name
- Filter communications by date range
- View related objects (all communications for a contact)

## Prerequisites

- Python 3.8+
- [Pipenv](https://pipenv.pypa.io/en/latest/) for virtual environment and package management  
  Install with:  
  ```bash
  pip install pipenv
  ```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/WillyKyeni3/contact-log-cli.git
   cd contact-log-cli
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Activate the environment**
   ```bash
   pipenv shell
   ```

## Usage

1. **Start the application**
   ```bash
   python lib/cli.py
   ```

2. **Available Commands**
   - Add a new contact
   - View all contacts
   - Update or delete a contact
   - Log a new communication for a contact
   - View communications for a specific contact
   - Search contacts by name
   - Filter communications by date range

   The CLI will guide you through each process with prompts.

## File Structure
```
contact-log-cli/
├── Pipfile
├── README.md
└── lib/
    └── models/
        ├── __init__.py
        ├── contact.py     
        └── communication.py 
    ├── cli.py 
    ├── debug.py 
    ├── database.py 
    ├── helpers.py 
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a pull request

Please write clear, concise commit messages and document new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pipenv](https://pipenv.pypa.io/)
- Python standard library
- 

---

If you have suggestions or found a bug, please open an issue on [GitHub Issues](https://github.com/WillyKyeni3/contact-log-cli/issues).
