# flask-demo

## requirements

* pipenv****
* python 3.7


## Installation

* clone repo https://github.com/avallbona/flask-demo
* change to folder where you cloned the repo
* with pipenv
    * `pipenv install`
    * `pipenv shell`
* with pip
    * python -m venv myenv
    * source bin/activate
    * pip install -r requirements.txt
* `cp .env.template to .env`
* fill the env vars
* `flask run`

## migrations

* to initializate the migratioins

    `flask db init`
    
* to generate the needed migrations

    `flask db migrate`
    
* to apply the generated migrations

    `flask db upgrade`

* to unapply the applied migrations

    `flask db downgrade`
