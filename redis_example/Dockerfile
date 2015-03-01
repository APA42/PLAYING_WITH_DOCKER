FROM python:2.7.7

MAINTAINER APA42 info@apa42.com

ENV PROJECT_DIR /opt/redis_example

# Create porject directory
RUN mkdir -p ${PROJECT_DIR}/
WORKDIR ${PROJECT_DIR}

# Update python installation with the requirements
COPY requirements.txt ${PROJECT_DIR}/
RUN pip install -r requirements.txt

# To modify files with other containers. Access to container's directory where is installed the program
VOLUME ${PROJECT_DIR}

# Execute main
ADD . ${PROJECT_DIR}/
CMD python redis_main.py
