## REST API in Python

The link to this tutorial is [REST API Crash Course](https://www.youtube.com/watch?v=qbLc5a9jdXo)

The link to the docs of this tutorial is [REST API Crash Course](https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit#)

`consume_api.py`  >>> This file is just basic `get` response from api


`api` This folder contain making own api.

before running `flask run` command always run this command `source run_flask_server.sh` in your terminal first, this will load the environment variable of Flask.
`flask run` starts the server in `localhost:5000` 


### CONNECTION WITH DATABASE

The things to do in terminal after writing code of creating database connection in `application.py` are:
1. Goto to folder where your main program file is located at
2. `python`
3. `from application import db` 
4. `from application import Drink` Drink here is a class name
5. `db.create_all()`
6. `drink = Drink(name='Grape Soda', description='Tastes like grapes')`
7. `drink` to return values in object drink
8. `db.session.add(drink)` or `db.session.add(Drink(name='Grape Soda', description='Tastes like grapes'))`
9. `db.session.commit()`
10. `Drink.query.all()` to fetch data
