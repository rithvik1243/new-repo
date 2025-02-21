from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://nagios.modak.com:7687"
username = "neo4j"
password = "ModakNeo4j"

driver = GraphDatabase.driver(uri, auth=(username, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            print(record)

# Example: Run a query to get all friends of Anudeep
query =""" MATCH (mentor:Person)-[:MENTORS]->(mentee:Person)
RETURN mentor.name AS Mentor, mentee.name AS Mentee
"""
run_query(query)

driver.close()
