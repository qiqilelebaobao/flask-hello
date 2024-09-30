# Python/Flask Tutorial for Visual Studio Code

* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.

* It also contains the *Dockerfile* and *uwsgi.ini* files necessary to build a container with a production server. The resulting image works both locally and when deployed to Azure App Service. See [Deploy Python using Docker containers](https://code.visualstudio.com/docs/python/tutorial-deploy-containers).

* To run the app locally:
  1. Run the command `cd hello_app`, to change into the folder that contains the Flask app.
  1. Run the command `set FLASK_APP=webapp` (Windows cmd) or `FLASK_APP=webapp` (macOS/Linux) to point to the app module.
  1. Start the Flask server with `flask run`.

## Install guide

  1. pip3 install flask_tutorial-1.0.0-py3-none-any.whl --target .
  1. pip3 install git+https://github.com/qiqilelebaobao/flask-hello.git --target .
  1. source hello/requirements/install.sh 

