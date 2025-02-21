from neo4j import GraphDatabase
 
# Create a driver instance (replace with your Neo4j server details)
uri = "bolt://nagios.modak.com:7687"  # Your Neo4j instance URL
username = "neo4j"  # Your Neo4j username
password = "ModakNeo4j"  # Your Neo4j password
 
# Create a driver instance
driver = GraphDatabase.driver(uri, auth=(username, password))
 
# Function to create two nodes in Neo4j
def create_two_nodes():
    with driver.session() as session:  # Create a session
        # Query to create two nodes with different properties
        query = """
        CREATE (n1:Person {name: 'Alic', age: 30})
        CREATE (n2:Person {name: 'Bb', age: 25})
        """
        session.run(query)  # Run the query
        print("Two nodes created!")
 
# Call the function to create nodes
create_two_nodes()
 
# Close the driver when done
driver.close()
 
 