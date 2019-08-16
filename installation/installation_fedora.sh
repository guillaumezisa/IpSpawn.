#!/bin/bash

################################################################################
# Date : 2019/08/14                                                            #
# Auteur : Guillaume Zisa                                                      #
# Version : Fedora.1                                                           #
# Titre : Installation des paquets nécéssaire au fonctionnement d'ipspawn      #
################################################################################

sudo dnf install python3 -y
sudo dnf install docker -y
sudo dnf install docker-compose -y
sudo pip3 install bottle
sudo pip3 install psycopg2
sudo pip3 install pygresql
