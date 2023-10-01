FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3
RUN mkdir /home/workdir
WORKDIR /home/workdir
COPY fl_logregression.py /home
ENTRYPOINT ["python3", "/home/fl_logregression.py"]

