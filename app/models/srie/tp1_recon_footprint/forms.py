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

class WhoisForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    submit = SubmitField('Submit')

class MetagoofilForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    fileTypes = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "File types list separated by commas"})
    
    submit = SubmitField('Submit')

class TheHarvesterForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    submit = SubmitField('Submit')

class MaryamForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    submit = SubmitField('Submit')