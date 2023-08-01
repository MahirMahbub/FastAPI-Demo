FROM python:3.11.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /srv/backend
#chown -R python /srv/backend
WORKDIR /srv/backend
COPY requirements.txt /srv/backend/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /srv/backend/