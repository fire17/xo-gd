
# Clean Structure for Pip Publish

'''



0 : Preperations:
    a. open an account over on PyPi: https://pypi.org/account/register/
    b. open an account over on TestPyPi: https://test.pypi.org/account/register/
    c. open a repo

    ######################
        THEN DO IT ALL ON GITHUB, new release, publish
    ######################
    ######################
1.
    cd to the folder that hosts the project
2.
    pip install cookiecutter
    cookiecutter https://github.com/wdm0006/cookiecutter-pipproject.git
3.
    cd xo #or project_name

4. #git init - skip if merge with existing

git init
git add -A
git commit -m 'Use Python Like You Never Have Before, Easy Acces To: Events and Triggers, Realtime MultiProcessing, Instant Dynamic DB, Filesytem & Web Watchdog, Sockets, API Server, Supports Fast Prototyping To Large Scale Systems'
git remote add origin https://github.com:fire17/xo-gd.git
git push -u origin master
git tag 3.1.3 -m 'GlobalData and XObject - Version 3 - Starlight'
git push --tags origin master
5.
    cd ~
    touch .pypirc
    nano .pypirc
6. copy from below
7. (add snippet from below)
8.
    cd -
    python setup.py register -r pypitest
    python setup.py sdist upload -r pypitest
'''

# COPY THIS:
'''
[distutils] # this tells distutils what package indexes you can push to
index-servers =
pypi
pypitest
[pypi]
repository: https://pypi.python.org/pypi
username: {{your_username}}
password: {{your_password}}
[pypitest]
repository: https://testpypi.python.org/pypi
username: {{your_username}}
password: {{your_password}}
'''

'''
xo versions
1 - wish - channels, triggers, multiprocessing
2 - rubicon - expando, selfNamed
3 - starlight - generic, env aware, sockets, api
4 - sunrise - os assistant, keyboard, mouse, easy vis, ai-kite
5 - agi
'''
