import requests
from bs4 import BeautifulSoup as bs
import wget

def download_hotel_data():
    """
    This function downloads hotel data from a specific URL and saves it as a CSV file.

    Returns:
    None
    """

    hotel_url = 'https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/'
    page = requests.get(hotel_url)
    soup = bs(page.content)
    links = soup.find_all("a", attrs={'title': 'Télécharger le fichier'})

    for a in links:
        print(a['href'])

    # Get the download link of the hotel data file
    data_link = links[1]['href']

    # Download the file and save it as 'hotel.csv' in the 'data' directory
    wget.download(data_link, out="data/hotel.csv")

