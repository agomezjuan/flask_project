import sys
from flask import render_template, redirect, url_for, request, abort, flash
from werkzeug.security import generate_password_hash, check_password_hash

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    users = User.query.all()
    return render_template('user/index.html', users=users)


def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not all([name, email, password]):
        flash('All fields are required')
        return redirect(url_for('register'))

    # Hash password
    password = generate_password_hash(password)

    # Create user
    user = User(username=name, email=email, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('user.index'))
    except Exception as e:
        flash('An error occurred while creating the user')
        return redirect(url_for('register'))


def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not all([email, password]):
        flash('All fields are required')
        return redirect(url_for('user.login'))

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('user.login'))

    # login_user(user)
    return redirect(url_for('user.index'))


def show(userId):
    # show a user profile for that user
    user = User.query.get(userId)


def update(userId):
    ...


def delete(userId):
    ...


def destroy(userId):
    ...
