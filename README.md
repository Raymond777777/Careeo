CareerGo-Demo

Primal stage of the project, goal being getting familiar with django and reaching MVP
File Structure

+---CareerGo-Demo
|   +---Lib                        (* Your own virtualenv file *)
|   |   +---site-packages
|   +---Scripts                    (* Your own virtualenv file *)
|   |   +---__pycache__
|   +---src                        (* Main Code For Project *)
|   |   +---CareerGo

Setup

    Windows --> Powershell
    MacOS --> Terminal

    Create a directory for the project.

    $ mkdir Dev

    Create the CareerGo folder, which contains various versions of CareerGO. Currently we are running CareerGo-Demo.

    $ mkdir CareerGo

    Install the virtual environment using pip.

        Make sure you are running Python 3.5 or higher:

        $ python --version

        Install virtualenv via pip:

        $ pip install virtualenv

        Check the install with freeze:

        $ pip freeze  or  $ pip list

    git clone at > ~\Dev\CareerGo, you should make sure your github ssh is already configured.

    $ ~/Dev/CareerGo/ > git clone <address of this repo>
    $ ~/Dev/CareerGo/ cd CareerGo-Demo

    Create virtual environment for CareerGo-Demo

    $ ~/Dev/CareerGo/CareerGo-Demo> virtualenv .

    At this point you should see the generated folder Lib, Scripts(bin on MacOS)

    Make sure to activate the virtual environment before you conduct testing or coding:

        Activate virtual environment

        Windows:

        $  ~/Dev/CareerGo/CareerGo-Demo> ./Scripts/activate

        MacOS:

        $  ~/Dev/CareerGo/CareerGo-Demo> source /bin/activate

        If activated successfully, a "(CareerDo-Demo)" tag will appear before the directory, this indicates other packages on your pc is no longer applicable under the virtual environment.

        $ (CareerGo-Demo) ~/Dev/CareerGo/CareerGo-Demo>

        Anytime you want to quit the virtual environment, simply type deactivate

    Install django under virtual environment

    (CareerGo-Demo) ~/Dev/CareerGo/CareerGo-Demo> pip install django==2.2.13

    Once django is installed, you can start the server to view the project

    $ (CareerGo-Demo) ~/Dev/CareerGo/CareerGo-Demo/src> python manage.py runserver

    This command will start the server and return your local host address. Copy that address into your browser. If you see "The install worked successfully! Congratulations!", your django is successfully configured and ready to go.

    IMPORTANT: Do not git push directly under CareerGo-Demo, since this will also push the virtualenv folders. Instead please store all the files under /src, and simply use git add src/.
