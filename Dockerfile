###############################################################################
# Environment
###############################################################################

FROM debian:jessie
MAINTAINER <hi@sparkgeo.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

###############################################################################
# Libraries
###############################################################################

# Post apt-get install
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python-dev \
    python-pip \
    supervisor \
    vim

RUN pip install --upgrade pip

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Gunicorn
####################################################
RUN groupadd webapps
RUN useradd webapp -G webapps
RUN mkdir -p /var/log/webapp/ && chown -R webapp /var/log/webapp/ && chmod -R u+rX /var/log/webapp/
RUN mkdir -p /var/run/webapp/ && chown -R webapp /var/run/webapp/ && chmod -R u+rX /var/run/webapp/
ADD ./config/gunicorn.conf /

# Nginx
####################################################
# RUN rm /etc/nginx/sites-enabled/default && rm /etc/nginx/sites-available/default
ADD ./config/webapp.nginxconf /etc/nginx/sites-enabled/

# Supervisor
####################################################
RUN mkdir -p /var/log/supervisor
ADD ./config/supervisor_conf.d/nginx.conf /etc/supervisor/conf.d/
ADD ./config/supervisor_conf.d/webapp.conf /etc/supervisor/conf.d/

##############################################################################
# Add source files
##############################################################################
WORKDIR /var/projects/webapp
ADD ./src .

##############################################################################
# Run
##############################################################################
EXPOSE 80 443
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
