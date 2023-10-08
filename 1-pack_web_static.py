#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """
    create a single .tgz file "version" from all the content web_static folder
    """
    currentDate = datetime.now().strftime("%Y%m%d%H%M%S")
    versionPath = "versions/web_static_{}.tgz".format(currentDate)
    cmd = "tar -cvzf {} web_static".format(versionPath)
    try:
        if not exists("versions"):
            local("mkdir versions")
        local(cmd)
        return versionPath
    except Exception:
        return None
