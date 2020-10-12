# scrape-google-search

Scraping Google search results in Python3.

## Environment

- Docker version 19.03.12, build 48a66213fe
- docker-compose version 1.26.2, build eefe0d31

## Stack

- Python 3.8.6


## Setup

```
$ docker-compose build
$ docker-compose up -d
```

## Run script

```
$ docker-compose exec docker-compose exec python python scrape.py {SOME KEYWORD}
```

or run script in the docker container.

```
$ docker-compose exec python bash
```

```
# python scrape.py {SOME KEYWORD}
```

## Options

```
# python scrape.py {SOME KEYWORD} --gl us --hl en --page 2 --num 20
```

|name|description|default|
|:--|:--|:--|
|gl|country code|us|
|hl|launguage code|en|
|page|page|1|
|num|number of results per page|10|