# Manga Scraper Flask

This is a simple manga scraper built in python with capablities of bypassing cloudflare thanks to the wonderful package [cloudscraper](https://pypi.org/project/cloudscraper/https:/).

## Supported Manga Website

* [X] Asura Scans
* [X] Reaper Scans
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

If you already are using Nginx Reverse Proxy Mangaer Then you can skip the optional Part or you need to setup the Optional Part first before starting it

```bash
docker-compose build
docker-compose up
```

The port it will expose to the network will be 80
