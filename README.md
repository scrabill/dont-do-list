# Don't Do List (WIP)

A Python and Flask MVC app of things you should probably try not to do.

## Installation

- Clone `https://github.com/scrabill/dont-do-list.git`
- CD into `dont-do-list`
- Create a `.env` file (`touch .env`)
- Add the following to the `.env` file

```python
DATABASE_URI=A://B@localhost:5432/dontdoapp
```

Where `A` is the name of your postgres database and `B` is postgres database username

- Run using `FLASK_APP=app.py flask run`