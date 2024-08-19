from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create an engine
engine = create_engine('sqlite:///example.db', echo=True)  # Use your database URL

# Define metadata object
metadata = MetaData()

# Define a table
user_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

# Create the table in the database
metadata.create_all(engine)
