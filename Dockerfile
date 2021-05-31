FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install tzdata
ENV TZ 'Europe/Rome'
CMD date +%c