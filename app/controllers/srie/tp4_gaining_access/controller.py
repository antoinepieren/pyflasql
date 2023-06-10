# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP4 - Gaining Access
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp4_gaining_access.forms import HydraForm


@login_required
def srie_tp4_gaining_access():
    """
        Logic for /srie/tp4_gaining_access/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp4_gaining_access')+'.html', username=username)

@login_required
def srie_tp4_hydra():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/nmapPort.html
        Login is required to view this page

        Pings 255 IP adresses

        Args:
            - network IP

        Returns:
            - list of active devices
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": HydraForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        ip_address = content["form"].ip_address.data
        usernames = content["form"].usernames.data
        passwords = content["form"].passwords.data
        # Generating files
        file = open("usernames.txt","w")
        file.write("\n".join(usernames.split(" ")))
        file.close()
        file = open("passwords.txt","w")
        file.write("\n".join(passwords.split(" ")))
        file.close()
        content["command_executed"] = f"hydra -L usernames.txt -P passwords.txt {ip_address} ftp -V"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_hydra')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_hydra')+'.html', content=content)
