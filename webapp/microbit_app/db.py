import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('ddl_schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('dml.sql') as f:
        db.executescript(f.read().decode('utf8'))

def init_demo():
    db = get_db()

    with current_app.open_resource('ddl_schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('dml_demo.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@click.argument('demo', default='')
@with_appcontext
def init_db_command(demo):
    """Create clean database with admin ('init-db demo' for demo data)"""
    if demo.lower() == "demo":
        init_demo()
        click.echo('Initialized the database with demo data')
    else:
        init_db()
        click.echo('Initialized the database')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)