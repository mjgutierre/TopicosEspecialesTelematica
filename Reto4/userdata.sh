#!/bin/bash
git clone https://github.com/mjgutierre/TopicosEspecialesTelematica.git
cd Reto4
chmod +x install.sh
./install.sh
sudo docker compose up
