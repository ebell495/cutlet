# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# set the working directory to /cutlet
WORKDIR /cutlet

# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        git \
        python3 \
        python3-pip && \
    apt-get clean

# Install dependencies
RUN pip3 install atheris fugashi[unidic-lite] jaconv pytest hypothesis setuptools_scm


# copy cutlet code to the docker image
COPY . /cutlet

# install cutlet
RUN cd /cutlet && \
    chmod +x fuzz/fuzz.py && \
    python3 setup.py install
