import sys
import urllib

import click
import requests
from bs4 import BeautifulSoup
from termcolor import colored


def scrape(query):
    URL = "https://google.com/search?q={query}".format(query=query)

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code != 200:
        print(colored("There's something wrong with google.", "red"))
        sys.exit(1)

    soup = BeautifulSoup(resp.content, "html.parser")
    results = ""
    for g in soup.find_all(class_='rc'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            results += colored(title, "green")
            results += "\n"
            results += colored(link, "blue")
            results += "\n\n"

    print(results)


@click.command()
@click.argument('query', nargs=-1)
def command(query):
    if len(query) == 0:
        print(colored("Please specify the search keyword as an argument.", "red"))
        sys.exit(1)

    scrape("+".join(query))

def main():
    command()

if __name__ == '__main__':
    main()
