from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, MetaData, create_engine, text, inspect

def save_to_database(df):
    """
    Saves the data to a SQLite database.

    Args:
        df (DataFrame): The data to be saved.
    """

    engine = create_engine('sqlite:///technical_test.db', echo=True)
    meta = MetaData()

    connection = engine.raw_connection()
    cursor = connection.cursor()

    hotel = Table(
        "hotel", meta,
        Column("data_de_classement", String),
        Column("classement", String),
        Column("nom_commercial", String),
        Column("adresse", String),
        Column("code_postal", String),
        Column("commune", String),
        Column("nombre_de_chambres", String),
        Column("concat", String),
        Column("code_postal_dept", String),
        Column("x", Float),
        Column("y", Float),
        Column("lon", Float),
        Column("lat", Float),
    )

    df.to_pandas().to_sql("hotel", con=engine)