FROM alpine:edge

RUN adduser -D kickoff

WORKDIR /home/kickoff

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev



COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY kickoff.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP kickoff.py

RUN chown -R kickoff:kickoff ./
USER kickoff

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
