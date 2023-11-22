# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange

class PasswordChangeForm(FlaskForm):
    new_password = StringField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "New password"})

    username = StringField(validators=[Length(min=4, max=300)])

    submit = SubmitField('Submit')
