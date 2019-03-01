FROM django

MAINTAINER "Mike Mutoro <mikemutoro@gmail.com>"

LABEL application="mobiflix-backend"

# Prevent dpkg errors
ENV TERM=xterm-256color


# Install current stable version of pip
RUN pip install pip==10.0.0

WORKDIR /

COPY requirements.txt

RUN pip install -r requirements.txt

COPY scripts/wait_for_postgres.sh /usr/local/bin/psql-h

RUN chmod +x /usr/local/bin/psql-h

COPY /content
