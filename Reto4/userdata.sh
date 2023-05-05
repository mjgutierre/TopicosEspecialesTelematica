#!/bin/bash
git clone https://github.com/mjgutierre/TopicosEspecialesTelematica.git
cd Reto4
chmod +x install.sh
./dockersetup.sh
sudo docker compose up
