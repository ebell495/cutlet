FROM python:3.8-bullseye

# Install dependencies
RUN pip3 install atheris fugashi[unidic-lite] jaconv pytest hypothesis setuptools_scm


# copy cutlet code to the docker image
COPY . /cutlet
# set the working directory to /cutlet
WORKDIR /cutlet

# install cutlet
RUN cd /cutlet && \
    chmod +x fuzz/romaji_decoder.py && \
    python3 -m pip install .
