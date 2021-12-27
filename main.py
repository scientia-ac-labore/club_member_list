from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError

app = Flask(__name__)

app_data = {}


def my_length_check(_, field):
    if field.data in app_data:
        raise ValidationError('Email already added')


class ClubMemberForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(max=64), Regexp(r'[a-zA-Z\s]+$'
                                                                                  , message="Incorrect value")])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=64), my_length_check])
    submit = SubmitField(label='Save')


@app.route("/", methods=['post', 'get'])
def main():
    form = ClubMemberForm(request.form)
    if request.method == 'POST':
        if form.validate():
            email = form.email.data
            app_data[email] = [form.name.data, date.today()]
            app.logger.debug('Added new member')
            form = ClubMemberForm()
        else:
            app.logger.debug(f'Error. Field {list(form.errors.keys())[0]}. Message {list(form.errors.values())[0][0]}')
    return render_template('main.html', data=app_data, form=form)


@app.before_request
def log_request_info():
    app.logger.debug('Request: %s', request.form.to_dict())

