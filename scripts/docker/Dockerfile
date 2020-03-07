# build from python 3.8
FROM python:3.8

# install requirements
COPY requirements.txt /opt/TutorialProject2/requirements.txt
RUN pip install --no-cache-dir -r /opt/TutorialProject2/requirements.txt

# copy source code and setup files
COPY data_explorer /opt/TutorialProject2/data_explorer
# COPY setup.py /opt/TutorialProject2
COPY setup.cfg /opt/TutorialProject2

# change working directory
WORKDIR /opt/TutorialProject2

# quick cleanup
# RUN chmod +x /entrypoint.sh

# volumes
VOLUME /opt/TutorialProject2/data_explorer