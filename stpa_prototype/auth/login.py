from flask import Blueprint, render_template, request, url_for, redirect

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     for
