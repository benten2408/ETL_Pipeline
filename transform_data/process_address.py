import polars as pl

def process_address_data():
    """
    Processes the address data.

    Returns:
        DataFrame: The processed address data.
    """
    pl_adresse = pl.read_csv("data/adresses-france.csv", separator=";", dtypes={"numero": pl.Utf8, "code_postal": pl.Utf8, "code_insee": pl.Utf8})

    pl_adresse = pl_adresse.fill_null(value="")

    col = pl_adresse[["numero", "rep", "nom_voie", "code_postal"]].apply(lambda x: "+".join(x))

    col = col.with_columns(
        pl.col('map').str.replace(r"\++", "+")
    )

    col = col.with_columns(
        pl.col('map').str.replace(r"\s++", "+")
    )

    col = col.with_columns(
        pl.col('map').str.to_lowercase()
    )

    pl_adresse_clean = pl.concat([pl_adresse, col], how="horizontal")

    pl_adresse_clean = pl_adresse_clean.rename({"map": "concat"})

    return pl_adresse_clean