FROM python:3.6

MAINTAINER David <davidvoler@gmail.com>
# set working directory to /app/

ENV INSTALL_PATH /app

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH
ADD ./requirements/dev.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD ./src ./

#Default command
CMD  python server.py
