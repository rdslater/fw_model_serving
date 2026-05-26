FROM python:3.10-slim

# Install required dependencies
RUN pip install flywheel-gear-toolkit requests

# Setup gear directory
ENV FLYWHEEL=/flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY manifest.json phase1_run.py ${FLYWHEEL}/

# Set working directory
WORKDIR ${FLYWHEEL}
