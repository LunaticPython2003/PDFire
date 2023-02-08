# Image to PDF Conversion App

A web application to convert image files to PDFs using Flask as the backend and Tailwind CSS as the frontend.

## [Click Here to View Deployment](https://pdfire.onrender.com)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Flask
- Tailwind CSS
- Python 3
- Pip

## Installing

Clone the repository and install the required packages.

```bash
git clone https://github.com/LunaticPython2003/PDFire.git
cd PDFire
pip install poetry
poetry install
```

## Start the production server

To run in production environment (or deploy in your server), in the root directory run the following commands in UNIX shell
**(Gunicorn doesn't run on Windows. It's very design is to take 'advantage of features in Unix/Unix-like kernels')**

```sh
gunicorn wsgi:app
```

Open your browser and go to http://localhost:5000 to view the app.

## Start the Flask development server

To run the development server, in the root directory, run the following command in your terminal

```bash
python -m flask --app main run
```

## Dependencies

- Flask
- Pillow

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The web framework used for the backend
- [Tailwind CSS](https://tailwindcss.com/) - The CSS framework used for the frontend
- [Python](https://www.python.org/) - The programming language used

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

Madhurjya Dasgupta & Pooranjoy Bhattacharya

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
