
from fabric.api import *
from fabric.operations import local

@task
def deploy():
    """docstring for deploy"""
    local("jekyll --no-auto")
    
    put("_site/*", "/mnt/svn/www/dysonclinic.co.uk", use_sudo = True)
    sudo("chown -R www-data:www-data /mnt/svn/www/dysonclinic.co.uk")