#!/bin/bash

################################################################################
# Date : 2019/08/14                                                            #
# Auteur : Guillaume Zisa                                                      #
# Version : Fedora.1                                                           #
# Titre : Installation des paquets nécéssaire au fonctionnement d'ipspawn      #
################################################################################

sudo dnf install python3.6 -y
sudo dnf install docker -y
sudo dnf install docker-compose -y
pip3 install --user --upgrade setuptools
pip3 install --user bottle
pip3 install --user psycopg2-binary
pip install --user py-postgresql
