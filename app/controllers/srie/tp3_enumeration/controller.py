# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP3 - Enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp3_enumeration.forms import TelnetForm, NmapBannerForm, NmapEnumForm, Enum4linuxForm, RpcclientForm

@login_required
def srie_tp3_enumeration():
    """
        Logic for /srie/tp3_enumeration/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)

@login_required
def srie_tp3_nmapBanner():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/nmapBanner.html

        Uses nmap to banner grab

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/nmapBanner.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapBannerForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"sudo nmap -sV -script=banner {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_nmapBanner')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_nmapBanner')+'.html', content=content)

@login_required
def srie_tp3_telnet():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/telnet.html
        Login is required to view this page

        Uses telnet to banner grab

        Args:
            - None.
        Returns:
            - rendered template view/templates/srie/tp3_enumeration/telnet.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TelnetForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and port number from the user interface (UI)
        ip_address = content["form"].ip_address.data
        port = content["form"].port.data
        content["command_executed"] = f"telnet {ip_address} {port}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_telnet')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_telnet')+'.html', content=content)

@login_required
def srie_tp3_nmapEnum():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/nmapEnum.html

        Uses nmap to enumerate users

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/nmapEnum.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapEnumForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"sudo nmap -script smb-enum-users.nse -p 445 {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_nmapEnum')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_nmapEnum')+'.html', content=content)

@login_required
def srie_tp3_enum4linux():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/enum4linux.html

        Uses enu4linux to enumerate users

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/enum4linux.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": Enum4linuxForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f" enum4linux -U {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_enum4linux')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_enum4linux')+'.html', content=content)

@login_required
def srie_tp3_rpcclient():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/rpcclient.html

        Uses rpcclient to enumerate users

        Args:
            - None

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/rpcclient.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": RpcclientForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f' rpcclient -U "" {ip_address}'
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_rpcclient')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_rpcclient')+'.html', content=content)
