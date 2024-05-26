#!/usr/bin/python3
"""
script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y%m%d%H%M%S")
    if not os.path.exists("versions"):
        os.makedirs("versions")
    archive_name = "versions/web_static_{}.tgz".format(
            formatted_datetime)

    try:
        local(
                "tar -cvzf {} web_static".format(
                    archive_name)
                )
        return archive_name
    except SystemExit:
        return None
