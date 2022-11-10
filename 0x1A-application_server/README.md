# 0x1A-application_server

## Task 0. Set up development with Python

**Step 0**: ssh into server

**Step 1**: Check if Python is already installed (it is!)

**Step 2**: Cloned `AirBnB_clone_v2` repo to root directory

**Step 3**: Install pip using `sudo apt-get install python3-pip`

**Step 4**: Install `virtualenv` using `pip` with `sudo pip3 install virtualenv`

**Step 5**: Create a new virtual environment with `virtualenv .venv-web_flask`

**Step 6**: Activate environment with `source .venv-web_flask/bin/activate`

**Step 7**: `pip3 install Flask`

**Step 8**: `sudo apt install net-tools`

**Step 9**: Run `sudo netstat -lpn` and `sudo ps auxf`

**Step 10**: Reassigned `datadog agent` server running on port `5000` to `50000` and cmd port from `5001` to `50001` in configuration file found in `/etc/datadog-agent/datadog.yaml`

**Step 11**: Restart Agent running as a service	`sudo service datadog-agent restart`

**Step 12**: `python3 -m web_flask.0-hello_route`
