# Flask Movie Manager

## Project Description
A web-based movie management system built with Flask. This application enables users to efficiently browse, search, add, and delete movies from a local database, providing an intuitive interface for organizing and managing a personal or shared video collection.

## Features
- Viewing the movies list
- Adding new movies
- Deleting movies
- Searching for movies

## Tech Stack
- **Framework:** [Flask](flask.palletsprojects.com)
- **Language:** Python 3.11
- **Database:** SQLite
- **Frontend:** HTML5, CSS3
- **Environment:** Virtualenv

## Installation & Setup
1. Clone or download this repository and navigate to the project directory
2. Create and activate a virtual environment
3. Install dependencies

### 1. Clone the repository
```bash
git clone <repository-url>
cd MovieDBFLASK
```
### 2. Create and activate virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
Before installing dependencies, make sure your virtual environment is activated:
```bash
pip install -r requirements.txt
```
To uninstall all dependencies listed in `requirements.txt` run:
```bash
pip uninstall -r requirements.txt -y
```
To list all installed packages, use:
```bash
pip freeze
```
You can also update your `requirements.txt` file with the current environment’s packages running:
```bash
pip freeze > requirements.txt
```

## Running the Application
```bash
flask run --debug
```

## Usage & Access
Once the server is running, you can access the application at:  
**Local Host**: http://127.0.0.1:5000  
**List of Movies**: View the list of all movies, delete selected movie, search for movie
**Add Movie**: Use the dedicated form to add movie to your database

## Author
Aleksandra Wilczyńska
Created as part of the postgraduate studies ISSI (Inżynieria Systemów Sztucznej Inteligencji) program at AGH University of Science and Technology.

## License
This project is part of an academic assignment for AGH University of Science and Technology, course " Wprowadzenie do technologii aplikacji internetowych". This project is released under the MIT License.
