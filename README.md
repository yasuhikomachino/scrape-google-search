# scrape-google-search

Scraping Google search results in Python3.

## Environment

- Docker 19.03.12
- docker-compose 1.26.2

## Stack

- Python 3.8.6
- mypy 0.79
- flake8 3.8.4
- black 20.8b1

## Setup

```
$ docker-compose build
$ docker-compose up -d
```

## Run script

```
$ docker-compose exec python python scrape.py {SOME KEYWORD}
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
|hl|language code|en|
|page|page|1|
|num|number of results per page|10|
