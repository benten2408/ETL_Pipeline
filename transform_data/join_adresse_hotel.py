

def join_data(pl_hotel, pl_adresse_clean):
    """
    Joins the hotel data and address data.

    Args:
        pl_hotel (DataFrame): The processed hotel data.
        df_pl_clean (DataFrame): The processed address data.

    Returns:
        DataFrame: The joined data.
    """
    pl_join = pl_hotel.join(pl_adresse_clean, on="concat", how="left").select(["DATE DE CLASSEMENT", "CLASSEMENT", "NOM COMMERCIAL", "ADRESSE", "CODE POSTAL","COMMUNE", "NOMBRE DE CHAMBRES", "concat", "CODE POSTAL DEPT", "x","y","lon","lat"])
    pl_join = pl_join.rename({"DATE DE CLASSEMENT": "date_classement", "CLASSEMENT": "classement", "NOM COMMERCIAL": "nom_commercial", "ADRESSE": "adresse", "CODE POSTAL": "code_postal", "COMMUNE": "commune", "NOMBRE DE CHAMBRES": "nombre_chambres", "concat": "concat", "CODE POSTAL DEPT": "code_postal_dept","x": "x", "y": "y", "lon": "lon", "lat": "lat"})

    return pl_join