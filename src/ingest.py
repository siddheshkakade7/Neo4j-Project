import pandas as pd
from connect import get_driver

driver = get_driver()
df = pd.read_csv("data/people.csv")

def ingest_data(tx, name, knows):
    tx.run("MERGE (a:Person {name: $name})", name=name)
    tx.run("MERGE (b:Person {name: $knows})", knows=knows)
    tx.run("""
        MATCH (a:Person {name: $name}), (b:Person {name: $knows})
        MERGE (a)-[:KNOWS]->(b)
    """, name=name, knows=knows)

with driver.session() as session:
    for _, row in df.iterrows():
        session.execute_write(ingest_data, row["name"], row["knows"])
