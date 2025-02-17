# Cardboard Calculator

A web-based calculator application built using Flask, allowing users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and square root. The app also includes user registration and login functionality.

## Features

- Basic arithmetic operations (+, -, *, ÷).
- Square root calculation.
- Clear and delete options for managing the current expression.
- User registration and login functionality with data stored in text files.
- Error handling for invalid expressions.

## Technologies Used

- Python (Flask framework)
- HTML
- CSS (for styling)

## Setup Instructions

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/Mukhdoom-Hammad-khan/Cardboard-Calculator.git

   
2. Install required dependencies:
   ```bash
   pip install flask

4. Run the application:
   ```bash
   python app.py


## Usage

Register a new account or log in with an existing one.
Perform calculations by clicking the buttons on the calculator interface.
Use the "Clear" button to reset the expression, and "Delete" to remove the last character.
Use the square root button (√) to calculate the square root of the expression.

## Flask Structure

Cardboard-Calculator/
│
├── app.py                   # Main Python file to run the Flask app
├── templates/               # Folder for HTML templates
│   ├── index.html           # Main page (calculator)
│   ├── login.html           # Login page
│   └── register.html        # Registration page
│
├── static/                  # Folder for static files (CSS)
│   └── css/                 # Folder for CSS files
│       └── style.css        # Main stylesheet
│
├── LICENSE                  # License file for the project
├── README.md                # Project description
└── requirements.txt         # File for listing dependencies (flask, etc.)

## Author
Mukhdoom Hammad Khan

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
