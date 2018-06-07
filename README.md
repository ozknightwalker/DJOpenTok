## Django OpenTok Example

### How to run

```bash
# create a virtualenv with python3
>> mkvirtualen venv
# install the required python packages
>> pip install -r requirements.txt
# run the django server
>> python manage.py runserver
```

### How to run using Docker

Note: This step requires [Docker](https://www.docker.com/) to be installed in your machine

```bash
# Build the docker image
>> docker build . -t {label}:{tag}
# Run the newly built docker image
>> docker run -it -p {port}:8000 {label}:{tag}
```
