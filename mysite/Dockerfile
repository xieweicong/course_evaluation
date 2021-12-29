FROM python:3.9
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt
RUN rm -rf /usr/src/app
COPY . /usr/src/app
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080", "--insecure"]