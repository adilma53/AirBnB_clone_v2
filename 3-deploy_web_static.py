#!/usr/bin/python3
""" module doc
"""
from fabric.api import task, local, env, put, run, runs_once
from datetime import datetime
import os

env.hosts = ['54.90.63.243', '54.90.4.180']


@runs_once
def do_pack():
    """
    create a single .tgz file "version" from all the content web_static folder
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    cmd = "tar -cvzf {} web_static".format(path)
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        local(cmd)
        return path
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """
    deploy archive to server
    """
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False


@task
def deploy():
    """
    function to run do_deploy
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)