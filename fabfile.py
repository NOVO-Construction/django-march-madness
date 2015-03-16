from os.path import dirname, join, normpath

from fabric.api import cd, env, local, run, sudo, shell_env
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
env.DJANGO_CONFIGURATION = 'Production'
env.DJANGO_SETTINGS_MODULE = 'config.production'
env.environment = 'production'


def install_software():
    "Install required software"
    sudo('yum -y groupinstall "Development Tools"')
    sudo("yum -y install git-core mercurial python-devel httpd mod_wsgi mod_ssl openssl "
         "vim sqlite mysql-devel libmysql-dev mysql rsync nginx memcached "
         "libxslt-devel libxml2-devell libyaml-devel python27 python27-devel nmap libjpeg-devel")


def managepy(cmd):
    manage = join(env.deploy_base, 'django-march-madness', 'manage.py')
    run('%s %s %s' % (env.python, manage, cmd))


def clean_pyc():
    sudo('find %(deploy_base)s -name "*.pyc" -exec rm -rf {} \;' % env)


def deploy_requirements():
    reqs = normpath(join(env.deploy_base, 'requirements', 'production.txt'))
    run('%s install -r %s' % (env.pip, reqs))


def reload_gunicorn():
    sudo("supervisorctl restart madness")


def push():
    """Push out new code to the server."""
    with shell_env(DJANGO_CONFIGURATION=env.DJANGO_CONFIGURATION, DJANGO_SETTINGS_MODULE=env.DJANGO_SETTINGS_MODULE):
        with cd("%(deploy_base)s" % env):
            run("git pull origin %(branch)s" % env)
        deploy_requirements()
        managepy('migrate')
        managepy('collectstatic --noinput --clear')
        reload_gunicorn()


def deploy_supervisor():
    with cd("/etc"):
        sudo("rm -rf /etc/supervisord.conf")
        sudo("rm -rf /etc/init.d/supervisord")
        put("%(local_root_path)s/config_files/supervisord.conf" % env, "/etc/supervisord.conf", use_sudo=True)
        put("%(local_root_path)s/bin/initscripts/supervisord" % env, "/etc/init.d/supervisord", use_sudo=True)
    sudo("chmod 755 /etc/init.d/supervisord")
    sudo("chkconfig --add supervisord")
    sudo("chkconfig supervisord on")
    sudo("supervisorctl reread")
    sudo("supervisorctl update")


def deploy_nginx():
    sudo("rm -rf /etc/nginx/nginx.conf")
    put("%(local_root_path)s/config_files/nginx.conf" % env, "/etc/nginx/nginx.conf", use_sudo=True)
    sudo("rm -rf /etc/nginx/mime.types")
    put("%(local_root_path)s/config_files/nginx-mime.types" % env, "/etc/nginx/mime.types", use_sudo=True)
    # Fix permissions SEE: http://stackoverflow.com/questions/10557927/server-response-gets-cut-off-half-way-through
    sudo("chown -R ec2-user:ec2-user /var/lib/nginx/")
    sudo("service nginx restart")
