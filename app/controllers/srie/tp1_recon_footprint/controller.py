# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output, CheckIf
from ....models.srie.tp1_recon_footprint.forms import WhoisForm, TheHarvesterForm, MaryamForm, MetagoofilForm

@login_required
def srie_home():
    """
        Handles the logic for /srie/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_home')+'.html', username=username)

@login_required
def srie_tp1_recon_footprint():
    """
        Handles the logic for /srie/tp1_recon_footprint/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp1_recon_footprint')+'.html', username=username)

@login_required
def srie_tp1_ipaddr():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/ipaddr.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/ipaddr.html with content passed as a context variable
        """
    # Create a dictionary to store the private and public IP addresses
    content = {"ip_address_private": "x.x.x.x", 
               "ip_address_public": "x.x.x.x",
               "cmd_ip_address_private": f"hostname -I",
               "cmd_ip_address_public": f"curl -s https://raphaelviera.fr/ismin/toolbox/my_ip.php"
               }
    # Uses get_shell_output() to execute a command in the shell and store the output in the dict.
    content["ip_address_private"] = get_shell_output(content["cmd_ip_address_private"])
    content["ip_address_public"]  = get_shell_output(content["cmd_ip_address_public"])
    return render_template(url_for('blueprint.srie_tp1_ipaddr')+'.html', content=content)



@login_required
def srie_tp1_whois():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/whois.html
        Login is required to view this page

        Prints information about a domain name.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/whois.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": WhoisForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data
        content["command_executed"] = f"curl -s https://raphaelviera.fr/ismin/toolbox/whois/whois.php?domain={domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_whois')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_whois')+'.html', content=content)

@login_required
def srie_tp1_theharvester():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/theharvester.html
        Login is required to view this page

        Print in whatever theHarvester finds idk how this works

        Args:
            - domain name

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/theharvester.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TheHarvesterForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Gets the Harvest
        domain = content["form"].domain.data
        content["command_executed"] = f"theHarvester -d {domain} -l 1000 -b urlscan"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_theharvester')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_theharvester')+'.html', content=content)

@login_required
def srie_tp1_metagoofil():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/metagoofil.html
        Login is required to view this page

        Downloads files hidden under a domain name

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/metagoofil.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": MetagoofilForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data
        fileTypes = content["form"].fileTypes.data
        content["command_executed"] = f"metagoofil -d {domain} -t {fileTypes} -o downloads"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_metagoofil')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_metagoofil')+'.html', content=content)

@login_required
def srie_tp1_maryam():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/maryam.html
        Login is required to view this page

        Print in whatever Maryam finds idk how this works

        Args:
            - domain name

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/maryam.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": MaryamForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Gets the whatever Maryam is supposed to get
        domain = content["form"].domain.data
        content["command_executed"] = f"maryam -e dns_search -d {domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_maryam')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_maryam')+'.html', content=content)
