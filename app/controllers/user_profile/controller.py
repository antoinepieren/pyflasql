# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Business logic for user profile
"""
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from ...models.app import PyFlaSQL
from ...models.sql import db, UserDB
from ..utils import get_shell_output
from ...models.user_profile.forms import PasswordChangeForm

def get_bcrypt():
    pyflasql_obj = PyFlaSQL()
    bcrypt = Bcrypt(pyflasql_obj.myapp)
    return bcrypt

@login_required
def user_profile():
    """
        Control the logout page.
        Login is required to view this page.

        Args:
            - None.

        Returns:
            - redirect to login page
        """
    username = current_user.username
    return render_template(url_for('blueprint.user_profile')+'.html', username=username)

@login_required
def password_reset():
    # Creates a dict to store the form and username. This dict is passed to the .html file.
    content = {"form": PasswordChangeForm(),"username":current_user.username}
    content["form"].new_password.data = request.args.get("new_password")
    content["form"].username.data = request.args.get("username")
    content["form"].submit.data = all((content["form"].new_password.data,
                                      content["form"].username.data))
    #if content["form"].validate(): never managed to get this to work
    if content["form"].submit.data : # Now this checks that there are values in the fields of the form
        # Fetching user
        user = UserDB.query.filter_by(username=content["form"].username.data).first()
        # Changing password
        bcrypt = get_bcrypt()
        hashed_password = bcrypt.generate_password_hash(content["form"].new_password.data)
        user.password = hashed_password
        db.session.commit()
        flash("Password changed successfully")
        return render_template(url_for('blueprint.password_reset')+'.html', content=content)
    return render_template(url_for('blueprint.password_reset')+'.html', content=content)
