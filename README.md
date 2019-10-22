# flask-demo

## Requirements

* pipenv
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
* `cp .env.template .env`
* fill the env vars
* `flask run`

## Migrations

* to initializate the migratioins

    `flask db init`
    
* to generate the needed migrations

    `flask db migrate`
    
* to apply the generated migrations

    `flask db upgrade`

* to unapply the applied migrations

    `flask db downgrade`

## Links

* repos used in the course
  * https://github.com/avallbona/flask-demo
  * https://github.com/avallbona/flask-sql-alchemy-demo
* python
  * [https://www.python.org](https://www.python.org/)
  * https://realpython.com/ (infinidad de tutoriales sobre el lenguaje y sus frameworks)
* flask
  * https://palletsprojects.com/p/flask/
* flask-sqlalchemy
  * https://flask-sqlalchemy.palletsprojects.com/en/2.x/ 
  * https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/ (tema de múltiples bases de datos)
* flask-restful
  * https://flask-restful.readthedocs.io/en/latest/ 
* marshmallow, serialization/deserialization of objects
  * https://marshmallow.readthedocs.io/en/stable/
* sentry, error monitoring
  * https://sentry.io/welcome/
* cookiecutter, creación de plantillas para nuevos proyectos
  * https://cookiecutter.readthedocs.io/en/latest/index.html
* cookiecutter del proyectos flask de tipo web
  * https://github.com/cookiecutter-flask/cookiecutter-flask
* cookiecutter de proyectos flask de tipo api rest
  * https://github.com/karec/cookiecutter-flask-restful
* pipenv (gestión de dependencias de aplicación y virtualenv)
  * https://pipenv.readthedocs.io/en/latest/
  * https://www.slideshare.net/AndreuVallbonaPlazas/py-day-mallorca-pipenv-python-dev-workflow-for-humans
* pytest (framework de testing)
  * http://pytest.org/en/latest/
  * https://www.slideshare.net/AndreuVallbonaPlazas/pybcn-pytest-recomendaciones-paquetes-bsicos-para-testing-en-python-y-django

