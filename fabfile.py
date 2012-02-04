
from fabric.api import *
from fabric.operations import local
from os.path import expanduser

env.user = 'ubuntu'
env.hosts = ['ec2d.logicalpractice.com']
env.key_filename = expanduser("~/.ssh/ec2d.pem")

@task
def deploy():
    """docstring for deploy"""
    local("jekyll --no-auto")
    
    put("_site/*", "/mnt/svn/www/dysonclinic.co.uk", use_sudo = True)
    sudo("chown -R www-data:www-data /mnt/svn/www/dysonclinic.co.uk")