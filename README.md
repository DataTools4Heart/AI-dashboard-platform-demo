# DT4H AI Dashboard - platform deployment
Build on top of an [openVRE](https://github.com/inab/dockerized_vre)-based analysis platform, the AI dashboard is a web-based interface designed to facilitate AI researchers and clinicians in the design, management, and **execution of federated learning (FL) experiments** across the DT4H federation. It provides a centralized and user-friendly environment to interact with various tools and services related to AI workflows and data analytics.

> **_NOTE:_**  Currently, the AI Dashboard is only for demonstration purposes.

## Components

The current repository contains the code for the deployment of a **fully containarized analysis platform**, including the following minimal set of services:

- Analysis platform web application (Virtual Research Environment ) ([openVRE](https://github.com/inab/openVRE/tree/dockerized))
- OIDC-compilant authentication server (Keycloak)
- batch queueing system (Sun Grid Engine, SGE based)

![architecture openvre (1)](https://user-images.githubusercontent.com/57795749/201643520-3e7b6cdf-b6c4-4985-9385-9a7b738174eb.png)


## Requirements
- Docker
- Docker compose

## Interdependent repositories
- Dashboard Demo Front-end: https://gitlab.bsc.es/fl/openvre-demo.git
- Dashboard Runner for FEM tasks: https://gitlab.bsc.es/inb/dt4h/FEM-runner

## Installation

##### Basic deployment 
1.	clone the current repository (check branch for master)
2.	cd to `dashboard-demo/front_end`
3.  git submodule add https://gitlab.bsc.es/FL/openvre-demo  (select appropriate branch)
4.	Configure `.env`:  HOSTNAME and IP_HOST. Check `…./config/globals.inc.php`
5.	Build images running `docker-compose build` 
6.	Start services running `docker-compose up -d`
7.	Enable queue system by executing "qconf -mconf" to modify min_uid=1000 (and min_gid) to 0

##### Load tools and datasets for M18 Demonstration
8.	Load initial data using `mongo_seed`. It loads mongodb contents (drop existing data, remove --drop from mongo_seed import.sh after first load)
9.	Load initial demo datasets  using `rsync front_end/openVRE/install/data/ to volumes/
