from bs4 import BeautifulSoup as bs
import requests
import wget
import gzip
import shutil

def download_address_data():
    """
    Retrieves the address data file.

    Returns:
        str: The file path of the downloaded file.
    """
    adresse = 'https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/'
    adresse_mini = 'https://adresse.data.gouv.fr'
    page = requests.get(adresse)
    soup = bs(page.content)
    links = soup.find_all("a")

    for a in links:
        if 'adresses-france' in a["href"]:
            print(a["href"])
            wget.download(adresse_mini + a["href"], out="data/adresses-france.csv.gz")
        else:
            pass
        
    with gzip.open("data/adresses-france.csv.gz", 'rb') as f_in:
        with open("data/adresses-france.csv", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

