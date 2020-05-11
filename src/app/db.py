import os
# ----------------------------------------------------------------------------
from databases import Database 
from sqlalchemy import create_engine, MetaData

# using the database URI and credentials that we just 
# configured in the Docker Compose file, 
DATABASE_URL= os.getenv("DATABASE_URL")

# we create a SQLAlchemy engine (used for communicating with the database)
# SQLAlchemy
engine = create_engine(DATABASE_URL)
# Along with a Metadata instance (used for creating the database schema).
metadata = MetaData()

# We create a new Database instance from databases.

prices = Table(
    "prices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("source", String(200)),
    Column("country", String(5)),
    Column("market", String(25)),
    Column("product_cat", String(50)),
    Column("product_agg", String(50)),
    Column("product", String(50)),
    Column("date", Datetime,),
    Column("retail", Integer),
    Column("wholesale", Integer),
    Column("currency", String(5)),
    Column("unit", String(5)),
    Column("active", String(5)),
    Column("udate", DateTime, default=func.now(), nullable=False),
    )

database = Database(DATABASE_URL)




