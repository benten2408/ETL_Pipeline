import pandas as pd
import polars as pl

def process_hotel_data():
    """
    Processes the hotel data.

    Reads the hotel data from a CSV file, filters it to include only hotels of type "HÔTEL DE TOURISME",
    performs some data transformations, and returns the processed data as a DataFrame.

    Returns:
        DataFrame: The processed hotel data.
    """
    
    df = pd.read_csv("data/hotel.csv", delimiter=';', encoding="ISO-8859-1", dtype={"CODE POSTAL": str})

    df_hotel = df[df["TYPE D'HÉBERGEMENT"] == "HÔTEL DE TOURISME"].reset_index(drop=True)

    df_hotel["ADRESSE"] = df_hotel["ADRESSE"].replace(" ", "+")
    df_hotel["ADRESSE"] = df_hotel["ADRESSE"].replace("++", "+")

    adresse = df_hotel["ADRESSE"]
    code_postal = [str(i) for i in df_hotel["CODE POSTAL"]]
    
    col_tmp = [add + "+" + code for add, code in zip(adresse, code_postal)]
    col_tmp = [i.lower() for i in col_tmp]

    df_hotel["concat"] = col_tmp
    
    new_col = df_hotel["CODE POSTAL"].apply(lambda x: x[:2])
    df_hotel["CODE POSTAL DEPT"] = new_col
    
    pl_hotel = pl.from_pandas(df_hotel)

    return pl_hotel