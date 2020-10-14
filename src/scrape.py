import sys
from urllib.parse import urlencode

import click
import requests
from bs4 import BeautifulSoup
from termcolor import colored


def scrape(query: str, options: str):
    url = "https://google.com/search?q={query}&{options}".format(
        query=query,
        options=options,
    )

    user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    headers: dict = {"user-agent": user_agent}
    response: requests.Response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(colored("There's something wrong with google.", "red"))
        sys.exit(1)

    soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")

    results: str = colored("URL: {url}".format(url=url), "magenta")
    results += "\n\n"

    for g in soup.find_all(class_="rc"):
        anchors: list = g.find_all("a")
        if anchors:
            link: str = anchors[0]["href"]
            title: str = g.find("h3").text
            results += colored(title, "green")
            results += "\n"
            results += colored(link, "blue")
            results += "\n\n"

    print(results)


@click.command()
@click.argument("query", nargs=-1)
@click.option("--gl", default="us")
@click.option("--hl", default="en")
@click.option("--num", default=10)
@click.option("--page", default=1)
def command(query, gl: str, hl: str, num: int, page: int):
    if len(query) == 0:
        print(colored("Please specify the search keyword as an argument.", "red"))
        sys.exit(1)

    options: dict = {
        "gl": gl,
        "hl": hl,
        "num": num,
        "start": num * (page - 1),
    }

    scrape("+".join(query), urlencode(options))


def main():
    command()


if __name__ == "__main__":
    main()
