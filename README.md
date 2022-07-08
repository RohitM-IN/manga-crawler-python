# Manga Scaraper API

This is a simple manga scraper made in python. It uses flask for API. This is not a fail proof but I will try to make it as good so it wont fail any request.

You can use this as a server to scrape Manga and use the API to implement it in your own application.

**Libraries used**

* Brotli
* Flask
* beautifulsoup4
* cloudscraper
* APScheduler - used to get new free working proxy
* numpy

## Supported Manga Website

* [X] Asura Scans
* [X] Reaper Scans
* [X] Flamescans.org
* [ ] Dragontea.ink
* [ ] Realmscans.com
* [ ] Isekai Scans
* [ ] MCReader
* [ ] FanFox
* [ ] Manganato
* [ ] Mangakakalot

## Installation

```bash
git clone https://github.com/RohitM-IN/manga-crawler-python.git MangaCrawler
cd MangaCrawler
```

```bash
pip install -r requirements.txt
flask run
```

## Api Endpoints

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/13642074-bbb9074f-98be-495a-b808-87e89ac8448c?action=collection%2Ffork&collection-url=entityId%3D13642074-bbb9074f-98be-495a-b808-87e89ac8448c%26entityType%3Dcollection%26workspaceId%3Dd73b682c-b872-43d0-9248-0bfb9998ef5f#?env%5BLocal%5D=W3sia2V5IjoidXJsIiwidmFsdWUiOiJodHRwOi8vMTI3LjAuMC4xOjUwMDAiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCIsInNlc3Npb25WYWx1ZSI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsInNlc3Npb25JbmRleCI6MH1d)

All Api Endpoints are defined in Postman Documentation
