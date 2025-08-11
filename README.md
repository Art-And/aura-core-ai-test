# AI Aura test

_Project which help us organize arrays._

## Getting Started 🚀

_These instructions will allow you to get a working copy of the project directly to your local machine, for development and testing purposes._

## Pre-requirements 📋

### Build with

_Main tools for project creation:_

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Python](https://www.python.org/) - 3.12.0 preferably, although you can use whatever you like and configure a venv with the required version
* [Docker](https://www.docker.com/) - containers


### Config 🔧
_Fist step, check your python version:_

_If you have no install python check [this link](https://www.python.org/downloads/) and install it:_
```
$ python --version
```

_Then install docker from [this link](https://www.docker.com/), and then verify the installation:_

```
$ docker --version
```

_Make sure to create you .env, please review the .env.example to config your own .env correctly_

_**WARNING**: If you don't config your .env correctly, maybe you will have an error._


_Once your .env is configured, next you have to build docker:_

```
$ docker-compose build --no-cache
```
_And that's it, you are done to begin._


## Who it works? 🛠️
 
Please run:
 ```
 $ docker-compose run --rm --service-ports api
 ```
 _Then apply the migrations(if is necessary, since there is a service in docker that runs them automatically)_
 ```
 $ docker-compose run --rm --service-ports api python manage.py migrate
 ```

And that's it, you will start to play!.

## Running test ⚙️

_For these cases we used [pytest](https://docs.pytest.org/en/stable/)_

_Please execute:_
```
$ docker-compose run --rm api py.test
```
_The tests will start running and once finished they should all pass without any problem (unless you broke it)._

_There is a small configuration file, which can be scaled if needed._


### And the style code tests? ⌨️

_We used [PEP-8](https://www.python.org/dev/peps/pep-0008/) along with [Zen de python](https://www.python.org/dev/peps/pep-0020/)_

_We use dependencies such as:_
* isort
* black
* flake8

_Development dependencies must be installed_


_To run your code test, just please execute:_

```
$ docker-compose run --rm api isort .
$ docker-compose run --rm api black .
$ docker-compose run --rm api flake8

```

## Extras 🎁

* Thank you very much for taking a look at my work, I hope you like it. 🤓
* Invite a beer 🍺 or a coffee ☕ to someone on your team
* Tell others about this project 📢

---
⌨️ with 💙 by [AndresIs](https://www.linkedin.com/in/andres-i/) 🌎