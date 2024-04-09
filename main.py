from extract_data.adresses import download_address_data
from extract_data.hotel import download_hotel_data
from transform_data.process_address import process_address_data
from transform_data.process_hotel import process_hotel_data
from transform_data.join_adresse_hotel import join_data
from load_data.load_data import save_to_database



# Retrieve hotel data
hotel_file = download_hotel_data()

# Retrieve address data
address_file = download_address_data()

# Process hotel data
pl_hotel = process_hotel_data()

# Process address data
pl_adresse_clean = process_address_data()

# Join hotel and address data
pl_join = join_data(pl_hotel, pl_adresse_clean)

# Save data to database
save_to_database(pl_join)
