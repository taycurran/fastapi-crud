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
database = Database(DATABASE_URL)