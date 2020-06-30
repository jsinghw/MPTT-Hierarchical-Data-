# MPTT-Hierarchical-Data-
The goal of this assignment is to learn about MPTT and different ways of working with it. Build a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure.

# Prerequisites
## Poetry
### Installation
#### osx / linux / bashonwindows install instructions
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
#### windows powershell install instructions
`(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python`

# Setup
1. Start virtual environment
  `poetry shell`

2. Run the django
`python manage.py runserver`
