# Dockerized OpenVRE

Deployment of a full openVRE-based analysis platform, including:

- openVRE module (frontend and backend): https://github.com/inab/openVRE/tree/dockerized
- Keycloak Authentication server
- Cluster SGE 

## Architecture

![architecture openvre (1)](https://user-images.githubusercontent.com/57795749/201643520-3e7b6cdf-b6c4-4985-9385-9a7b738174eb.png)

## Installation (provisional)

Require Docker/Docker-compose

1.	clone https://gitlab.bsc.es/inb/dt4h/GUI_Mockup.git (check branch for master o eucaim_fld)
2.	cd to  GUI_Mockup/front_end ans clone there https://gitlab.bsc.es/inb/dt4h/openVRE  (select branch)
3.	Configure .env:  HOSTNAME and IP_HOST y comprovar …./config/globals.inc.php
4.	docker-compose build
5.	docker-compose up -d 
6.	mongo_seed loads mongodb contents (drop existing data, remove --drop from mongo_seed import.sh after first load)
7.	rsync front_end/openVRE/install/data/ to volumes/shared_data
8.	at docker sgecore, execute "qconf -mconf" to modify min_uid=1000 (and min_gid) to 0

Mockup Data adapted to DT4H 
