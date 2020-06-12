# from geopy.geocoders import Nominatim
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import csv_importer, User

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


# Route for main page of bay area tracker exhibit carousels
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/bayareatracker')
def bayareatracker():
    exhibits = csv_importer()
    return render_template('bayareatracker.html', exhibits=exhibits)


# Route for Exhibits API
@app.route('/bayareatracker/api/v1/exhibits', methods=['GET'])
def get_exhibits():
    exhibits = csv_importer()
    return jsonify({'exhibits': exhibits})


# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)