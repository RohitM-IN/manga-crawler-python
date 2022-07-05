# Manga Scraper Flask

This is a simple manga scraper built in python with capablities of bypassing cloudflare thanks to the wonderful package [cloudscraper](https://pypi.org/project/cloudscraper/https:/).

## Supported Manga Website

* [X] Asura Scans
* [ ] Reaper Scans
* [ ] Isekai Scans
* [ ] Flamescans.org
* [ ] MCReader
* [ ] FanFox
* [ ] Manganato
* [ ] Mangakakalot

## Installation

We recommand you use docker for this since its easy to setup

```bash
git clone https://github.com/RohitM-IN/manga-crawler-python.git MangaCrawler
cd MangaCrawler
```

If you already are using Nginx Reverse Proxy Mangaer Then you can skip the optional Part

```bash
docker-compose build
docker-compose up
```

The port it will expose to the network will be 80

### Optional: To setup Nginx Reverse Proxy Manager

Create a Network by name `nginxproxymanager`

```bash
docker network create 
```

```yml
version: '3.8'

services:
  nginxproxymanager:
    container_name: nginxproxymanager
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80' # HTTP
      - '81:81' # Nginx Dashboard
      - '443:443' # HTTPS
      - '3306:3306' # MySQL
    environment:
      X_FRAME_OPTIONS: "sameorigin"
      # MySQL Database Credentials
      DB_MYSQL_HOST: "mysql"
      DB_MYSQL_PORT: 3306
      DB_MYSQL_USER: "" # setup your own user
      DB_MYSQL_PASSWORD: "" # setup your own password
      DB_MYSQL_NAME: "" # setup your own Database
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
      # -  ./_hsts.conf:/app/templates/_hsts.conf:ro


networks:
  default:
    external:
      name: nginxproxymanager
```

Optional: You can setup Sql Server with the following example

```yml
version: '3.5'

services:
  mysql:
    container_name: mysql
    image: mysql
    restart: always
    volumes:
      - ./var/lib/mysql:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: mysupersecretpassword


  phpmyadmin:
    container_name: phpmyadmin
    image: phpmyadmin/phpmyadmin:latest
    restart: always
    volumes:
      - ./phpmyadmin.config.user.inc.php:/etc/phpmyadmin/config.user.inc.php
    environment:
      PMA_HOST: mysql

networks:
  default:
    name: nginxproxymanager
    external: true
```
