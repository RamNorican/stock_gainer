# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True


# Copy local code to the container image.
ENV APP_HOME /src

WORKDIR $APP_HOME

COPY . ./

RUN pip install ./src
# Install production dependencies.
#RUN pip install --no-cache-dir -r requirements.txt
CMD [ "/bin/sh" ]