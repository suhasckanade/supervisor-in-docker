FROM ubuntu:latest
RUN apt update
RUN apt install -y supervisor
RUN mkdir -p /var/log/supervisor /home/docker-supervisorctl
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY *.py /home/docker-supervisorctl/
RUN touch /home/docker-supervisorctl/process.log
CMD /usr/bin/supervisord && /bin/bash