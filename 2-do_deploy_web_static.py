#!/usr/bin/python3
"""
deploying a basic web static
"""
from datetime import datetime
import os
from fabric.api import run, env, put, local, task

env.hosts = ["35.175.63.217", "100.25.194.58"]


@task
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


@task
def do_deploy(archive_path):
    """
    deploy archive to server
    """
    if not archive_path or not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp')
    
    try:
        if not os.path.exists(archive_path):
            return False

        fileWithExtension = os.path.basename(archive_path)
        fileWithoutExtension, ext = os.path.splitext(fileWithExtension)
        releasePath = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(releasePath, fileWithoutExtension))
        run("mkdir -p {}{}/".format(releasePath, fileWithoutExtension))
        run("tar -xzf /tmp/{} -C {}{}/".format(fileWithExtension, releasePath, fileWithoutExtension))
        run("rm /tmp/{}".format(fileWithExtension))
        run("mv {0}{1}/web_static/* {0}{1}/".format(releasePath, fileWithoutExtension))
        run("rm -rf {}{}/web_static".format(releasePath, fileWithoutExtension))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(releasePath, fileWithoutExtension))

        print("New version deployed!")
        return True

    except Exception:
        return False