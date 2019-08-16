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
sudo pip3 install bottle
sudo pip3 install psycopg2
sudo pip3 install pygresql
