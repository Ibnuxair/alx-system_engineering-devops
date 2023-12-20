#!/bin/bash
# Author: Blain Muema
# Github: @octocatblain

# This script will uninstall mysql server and its dependencies

# stop mysql server
sudo systemctl stop mysql

# Remove mysql
sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-* -y

# Remove dependencies
sudo apt-get autoremove -y

# clean up
sudo apt-get autoclean -y

# Verify uninstallation was successful
mysql --version
