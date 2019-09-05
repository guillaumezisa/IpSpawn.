#!/bin/bash

################################################################################
# Date : 2019/08/14                                                            #
# Auteur : Guillaume Zisa                                                      #
# Version : Debian.1                                                           #
# Titre : Installation des paquets nécéssaire au fonctionnement d'ipspawn      #
################################################################################

sudo apt install python3 -y
sudo apt install docker -y
sudo apt install docker-compose -y
sudo apt-get install postgresql-devel -y
pip3 install --user --upgrade setuptools
pip3 install --user bottle
pip3 install --user psycopg2-binary
pip3 install --user pygresql
