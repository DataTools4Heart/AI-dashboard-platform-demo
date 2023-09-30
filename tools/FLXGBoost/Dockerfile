FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3
RUN mkdir /home/workdir
WORKDIR /home/workdir
COPY site_discovery.py /home
ENTRYPOINT ["python3", "/home/site_discovery.py"]

