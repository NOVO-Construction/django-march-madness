from os.path import dirname, join, normpath

from fabric.api import cd, env, local, run, sudo
from fabric.operations import put

env.hosts = ['madness.novoconstruction.com']
env.user = 'ec2-user'
env.deploy_base = '/home/ec2-user/madness'
env.virtualenv = '/home/ec2-user/.virtualenvs/madness'
env.git_dir = normpath(join(env.deploy_base, '.git'))
env.python = normpath(join(env.virtualenv, 'bin', 'python'))
env.pip = normpath(join(env.virtualenv, 'bin', 'pip'))
env.branch = 'master'
env.local_root_path = path = dirname(__file__)


def install_software():
    "Install required software"
    sudo('yum -y groupinstall "Development Tools"')
    sudo("yum -y install git-core mercurial python-devel httpd mod_wsgi mod_ssl openssl "
         "vim sqlite mysql-devel libmysql-dev mysql rsync nginx memcached "
         "libxslt-devel libxml2-devell libyaml-devel python27 python27-devel nmap libjpeg-devel")


def managepy(cmd):
    manage = join(env.deploy_base, 'sentinel', 'manage.py')
    run('%s %s %s' % (env.python, manage, cmd))


def clean_pyc():
    sudo('find %(deploy_base)s -name "*.pyc" -exec rm -rf {} \;' % env)


def deploy_requirements():
    reqs = normpath(join(env.deploy_base, 'requirements', 'production.txt'))
    run('%s install -r %s' % (env.pip, reqs))


def reload_gunicorn():
    sudo("supervisorctl restart madness")


def push():
    with cd("%(deploy_base)s" % env):
        run("git pull origin %(branch)s" % env)
    deploy_requirements()
    managepy('migrate')
    clean_pyc()
    reload_gunicorn()
