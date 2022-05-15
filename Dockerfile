# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# set the working directory to /phonemizer
WORKDIR /cutlet

# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        git \
        python3 \
        python3-pip && \
    apt-get clean

# pytest needs to be installed through pip to make sure we have a recent version
RUN pip3 install atheris fugashi[unidic-lite] jaconv pytest hypothesis setuptools_scm

# # tests expect python to be available as executable 'python' not 'python3'
# RUN ln -s /usr/bin/python3 /usr/bin/python

# copy the phonemizer code within the docker image
COPY . /cutlet

# install phonemizer and run the tests
RUN cd /cutlet && \
    chmod +x fuzz/fuzz.py && \
    python3 setup.py install
