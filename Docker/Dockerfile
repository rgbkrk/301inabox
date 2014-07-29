# DOCKER-VERSION 1.0.1

#Using Ubuntu 14.04
FROM	ubuntu:trusty

# Update the system and install files
ENV	DEBIAN_FRONTEND noninteractive
RUN	apt-get update
RUN	apt-get -y upgrade
# Random packages that may or may not be needed
RUN	apt-get -y install python-pip wget git libldap2-dev libsasl2-dev libxml2-dev libxslt1-dev lib32z1-dev python-dev tmux screen expect vim
RUN	pip install virtualenv

# More things go here
