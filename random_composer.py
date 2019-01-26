import random
from b4 import BeautifulSoup
import click
import requests


@click.command()
@click.option("-n", "--number", default=1)
def get_composer(number):
    wiki_composer_page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_classical_music_composers_by_era"
    )
    if not wiki_composer_page.ok:
        print("Failed to download list of composers")
        raise SystemExit(1)
    composer_soup = BeautifulSoup(wiki_composer_page.text, "html.parser")
    timelines = composer_soup.find_all("div", class_="timeline-wrapper")
    composer_elements = []
    for item in timelines:
        composer_elements.extend(item.find_all("area"))
    composers = [comp['title'] for comp in composer_elements]

    choices = random.choices(composers, k=number)
    for item in choices:
        print(item)


if __name__ == "__main__":
    get_composer()
