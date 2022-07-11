# Manga Scaraper API

This is a simple manga scraper made in python. It uses flask for API. This is not a fail proof but I will try to make it as good so it wont fail any request.

You can use this as a server to scrape Manga and use the API to implement it in your own application.

**Libraries used**

* Brotli
* Flask
* beautifulsoup4
* cloudscraper
* APScheduler - used to get new free working proxy

## Supported Manga Website

* [X] [Asura Scans](https://asurascans.com/) [ Theme Mangastream ]
* [X] [Reaper Scans](https://reaperscans.com/) [ Theme Madara ]
* [X] [Flame Scans](https://flamescans.org/) [ Theme MangaReader ]
* [X] [Dragon Tea](https://dragontea.ink) [ Theme Madara ]
* [X] [Realm Scans](https://realmscans.com) [ Theme MangaReader ]
* [ ] [Alpha Scans](https://alpha-scans.org) [ Theme MangaReader ]
* [ ] [Leviatan Scans](https://leviatanscans.com/hym/) [ Theme Madara ]
* [ ] [Webdex Scan](https://webdexscan.blogspot.com/) [ Theme **ZeistManga v5** for bloggers ]
* [ ] [Mangadex](https://mangadex.org) [ Theme Mangadex V5 ]
* [ ] [Isekai Scans](https://isekaiscan.com) [ Theme Madara but page as navigator ]
* [ ] [MC Reader (manga-raw)](https://www.mcreader.net/) [ Using Django Theme Unknown ]
* [ ] [FanFox (Manga Fox)](https://fanfox.net/)) [ Theme Name Unknown ]
* [ ] [Manganato](https://manganato.com)[ Using CodeIgniter Theme Name Unknown ]
* [ ] [Mangakakalot](https://mangakakalot.com/) [ Using CodeIgniter Theme Name Unknown ]

IF I have Time I will add some other Manga Bloggers 

* [ ] [Blueberry Scans](https://blueberryscans.blogspot.com/)
* [ ] [Hachimitsu Scans (hachimitsu-scans.blogspot.com)](https://hachimitsu-scans.blogspot.com/) [ A challange for me XD using google drive or mediafire and compressing with RAR :( ]
* [ ] ~~[Nux Scans](https://nuxscans.blogspot.com/)~~ [ Abondoned for more than 10 months]

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

## Current Issues

1. Madara - any thing with post method is an issue need to use playwrite or something for that
