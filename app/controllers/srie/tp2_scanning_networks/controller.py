# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP2 - Scanning Networks
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp2_scanning_networks.forms import PingAddrForm, FPingForm, NmapNetworkForm, NmapPortForm, TracerouteForm


@login_required
def srie_tp2_scanning_networks():
    """
        Logic for /srie/tp2_scanning_networks/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networks/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp2_scanning_networks')+'.html', username=username)

@login_required
def srie_tp2_pingaddr():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/pingaddr.html
        Login is required to view this page

        Pings an address n times
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/pingaddr.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": PingAddrForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        ip_address = content["form"].ip_address.data
        npings = content["form"].npings.data
        content["command_executed"] = f"ping -c {npings} {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_pingaddr')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_pingaddr')+'.html', content=content)

@login_required
def srie_tp2_fping():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/fping.html
        Login is required to view this page

        Pings 255 IP adresses

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/fping.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": FPingForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"fping -s -g {ip_address}.1 {ip_address}.255"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_fping')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_fping')+'.html', content=content)

@login_required
def srie_tp2_nmapNetwork():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/nmapNetwork.html
        Login is required to view this page

        Uses nmap to scan the network to have a list of active devices

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/nmapNetwork.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapNetworkForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"nmap -T3 -sn {ip_address}.0/24"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_nmapNetwork')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_nmapNetwork')+'.html', content=content)

@login_required
def srie_tp2_nmapPort():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/nmapPort.html
        Login is required to view this page

        Uses nmap to scan a device for open ports

        Args:
            - None

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/nmapPort.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapPortForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"sudo nmap -sS -Pn {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_nmapPort')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_nmapPort')+'.html', content=content)

@login_required
def srie_tp2_traceroute():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/traceroute.html
        Login is required to view this page

        Does traceroute

        Args:
            - None

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/traceroute.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TracerouteForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address from the user interface (UI)
        ip_address = content["form"].ip_address.data
        content["command_executed"] = f"traceroute {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_traceroute')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_traceroute')+'.html', content=content)
