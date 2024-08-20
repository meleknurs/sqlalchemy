from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select, delete

# Create an engine
engine = create_engine('sqlite:///example.db', echo=True)

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

# Clear the table before inserting new rows
with engine.connect() as connection:
    connection.execute(delete(user_table))
    connection.commit()

# Insert multiple rows at once using connection.execute directly
rows_to_insert = [
    {"name": "John Doe", "age": 29},
    {"name": "Jane Doe", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24}
]

# Execute the insert statement
with engine.connect() as connection:
    connection.execute(user_table.insert(), rows_to_insert)
    connection.commit()

# Create a select statement to fetch all rows
select_stmt = select(user_table)

# Execute the select statement and fetch results
with engine.connect() as connection:
    result = connection.execute(select_stmt)

    for row in result:
        print(row)
