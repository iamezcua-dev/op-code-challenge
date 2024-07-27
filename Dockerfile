# Use an official Python runtime as a parent image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /opanga_configuration_parser

# Add python scripts to the docker image
COPY . /opanga_configuration_parser

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r dev-requirements.txt

# Tell Python this is the base dir for executing our program
ENV PYTHONPATH="/opanga_configuration_parser"