from connect import get_driver

driver = get_driver()

def get_friends(tx, name):
    result = tx.run("""
        MATCH (p:Person {name: $name})-[:KNOWS]->(friend)
        RETURN friend.name AS name
    """, name=name)
    return [r["name"] for r in result]

with driver.session() as session:
    friends = session.execute_read(get_friends, name="Alice")
    print("Alice knows:", friends)
