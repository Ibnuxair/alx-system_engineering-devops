#!/bin/bash
# Author: Blain Muema
# Github: @octocatblain

# This script will install mysql version 5.7*

# Change permissions for signature.key file
sudo chmod 644 signature.key

# signature.key is a file from (https://intranet.alxswe.com/rltoken/Zzs_TLRYjWWFxjJRArmFcQ)
sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-get update

# Add this key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C

# Check available versions
sudo apt-cache policy mysql-server

# Install mysql 5.7*
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y

#check installed mysql version
mysql --version
