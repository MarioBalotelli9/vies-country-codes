from bs4 import BeautifulSoup
import requests
from constants import VIES_URL, HEADERS


def __get_page_content(url: str, headers: dict) -> bytes:
    """
    Gets the html content of the Vies page.

    :param url: Vies VAT number verification page url.
    :param headers: Headers for the request
    :return Content of the requested page.
    """
    req = requests.get(url, headers)
    return req.content


def __get_list_from_soup(html_content: bytes) -> list:
    """
    Gets the list of countries from the html content.

    :param html_content: Content of the Vies VAT number verification page.
    :return List of country codes.
    """
    soup = BeautifulSoup(html_content, "lxml")
    country_options = soup.find(id="countryCombobox").findAll("option")
    raw_list = list(map(lambda option: option["value"], country_options))
    return raw_list[1:]


def get_iso_codes():
    """
    Gets the list of countries from the Vies VAT number verification page..

    :return List of country codes.
    """
    html_content = __get_page_content(VIES_URL, HEADERS)
    codes_list = __get_list_from_soup(html_content)
    return codes_list
