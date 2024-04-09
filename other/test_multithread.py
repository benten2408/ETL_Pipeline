"""

for add, code in zip(adresse, code_postal):
    print(add)

    requete = requests.get("https://api-adresse.data.gouv.fr/search/?q=" + add + "&postcode=" + code).json()

    try:
        coordinates = requete["features"][0]["geometry"]["coordinates"]
        a.append(coordinates[0])
        b.append(coordinates[1])
    except:
        "No coordinates"



def func(url):
    requete = requests.get(url).json()

    if requete["features"] != []:
        coordinates = requete["features"][0]["geometry"]["coordinates"]
        a.append(coordinates[0])
        b.append(coordinates[1])
    else:
        pass
    
processed_results = []

start = time.perf_counter()
threads = []
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(func, url) for url in urls]
        for f in concurrent.futures.as_completed(results):
            processed_results.append(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
"""