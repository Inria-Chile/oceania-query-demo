ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER
USER root
COPY . /opt/app
WORKDIR /opt/app
RUN pip3 install oceania-query-fasta
# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID