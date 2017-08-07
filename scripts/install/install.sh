#!/bin/bash -xe


# Установка на Ubuntu 16.04
# Предполагается наличие: bash, python3.5-dev, cron


sudo apt-get update


# Подкачка

sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab


# Локали

sudo locale-gen ru_RU.UTF-8
sudo update-locale LANG=ru_RU.UTF-8 LANGUAGE=ru_RU:


# Curl

sudo apt-get install build-essential curl


# PIP

curl -sL https://bootstrap.pypa.io/get-pip.py | sudo -HE python3 -


# NodeJS

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install nodejs


# Electron environment

sudo apt-get install libgtk2.0-0 libgconf-2-4 libasound2 libxtst6 libxss1 libnss3 xvfb


# Mongo

gpg --keyserver keyserver.ubuntu.com --recv EA312927
gpg --export D68FA50FEA312927 | sudo apt-key add -

echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update
sudo apt-get install mongodb-org

sudo cp /lib/systemd/system/mongod.service
systemctl enable mongod


# LevelDB

sudo apt-get libleveldb1v5 libleveldb-dev


# Установка Python-пакетов

cd ..
sudo -H python3 -m pip install -r requirements.txt
npm install
cd install


# Настройка Cron

sudo cp scripts/install/betrobot.cron /etc/cron.hourly/betrobot


# Инициализация

mkdir data
mkdir data/betcityDatesHtml
mkdir data/pickables
mkdir data/providers
mkdir tmp
mkdir tmp/update
mkdir tmp/update/headers
mkdir tmp/update/betarch
mkdir tmp/update/betcity
mkdir tmp/update/whoscored
mkdir tmp/update/intelbet

./scripts/install/init_db.py
