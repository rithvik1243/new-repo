from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://nagios.modak.com:7687"
username = "neo4j"
password = "ModakNeo4j"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to create nodes and relationships
def create_nodes_and_relationships():
    with driver.session() as session:
        query = """
        CREATE (anudeep:Person {name: 'Anudeep', age: 22, city: 'Hyderabad', college: 'IIT Hyderabad', branch: 'CSE', hobby: 'Music'})
        CREATE (sunny:Person {name: 'Sunny', age: 23, city: 'Warangal', college: 'NIT Warangal', branch: 'ECE', hobby: 'Cricket'})
        CREATE (vamshi:Person {name: 'Vamshi', age: 24, city: 'Karimnagar', college: 'JNTU Hyderabad', branch: 'Mechanical', hobby: 'Photography'})
        CREATE (tarun:Person {name: 'Tarun', age: 22, city: 'Nizamabad', college: 'OU Hyderabad', branch: 'Civil', hobby: 'Gaming'})
        CREATE (dinakar:Person {name: 'Dinakar', age: 23, city: 'Khammam', college: 'CBIT', branch: 'EEE', hobby: 'Reading'})
        CREATE (bhanu:Person {name: 'Bhanu', age: 24, city: 'Mahbubnagar', college: 'VNR VJIET', branch: 'IT', hobby: 'Painting'})
        CREATE (nithin:Person {name: 'Nithin', age: 22, city: 'Siddipet', college: 'BITS Pilani', branch: 'Aerospace', hobby: 'Traveling'})
        CREATE (rithvik:Person {name: 'Rithvik', age: 23, city: 'Adilabad', college: 'IIIT Hyderabad', branch: 'AI', hobby: 'Coding'})
        
        CREATE (anudeep)-[:FRIENDS_WITH]->(sunny)
        CREATE (sunny)-[:FRIENDS_WITH]->(vamshi)
        CREATE (vamshi)-[:FRIENDS_WITH]->(tarun)
        CREATE (tarun)-[:FRIENDS_WITH]->(dinakar)
        CREATE (dinakar)-[:FRIENDS_WITH]->(bhanu)
        CREATE (bhanu)-[:FRIENDS_WITH]->(nithin)
        CREATE (nithin)-[:FRIENDS_WITH]->(rithvik)
        CREATE (rithvik)-[:FRIENDS_WITH]->(anudeep)
        
        CREATE (anudeep)-[:FRIENDS_WITH]->(vamshi)
        CREATE (sunny)-[:FRIENDS_WITH]->(bhanu)
        CREATE (tarun)-[:FRIENDS_WITH]->(rithvik)
        CREATE (dinakar)-[:FRIENDS_WITH]->(nithin)
        
        CREATE (anudeep)-[:MENTORS]->(rithvik)
        CREATE (sunny)-[:COLLABORATES_WITH]->(tarun)
        CREATE (vamshi)-[:KNOWS]->(dinakar)
        CREATE (bhanu)-[:GUIDES]->(nithin)
        CREATE (nithin)-[:PARTNERS_WITH]->(sunny)
        
        CREATE (rithvik)-[:WORKS_WITH]->(dinakar)
        CREATE (bhanu)-[:SHARES_IDEAS_WITH]->(tarun)
        CREATE (sunny)-[:PROJECT_PARTNER]->(nithin)
        CREATE (vamshi)-[:TEAMMATE]->(anudeep)
        CREATE (tarun)-[:DISCUSS_WITH]->(dinakar)
        
        CREATE (anudeep)-[:STUDIES]->(:Branch {name: 'CSE'})
        CREATE (sunny)-[:STUDIES]->(:Branch {name: 'ECE'})
        CREATE (vamshi)-[:STUDIES]->(:Branch {name: 'Mechanical'})
        CREATE (tarun)-[:STUDIES]->(:Branch {name: 'Civil'})
        CREATE (dinakar)-[:STUDIES]->(:Branch {name: 'EEE'})
        CREATE (bhanu)-[:STUDIES]->(:Branch {name: 'IT'})
        CREATE (nithin)-[:STUDIES]->(:Branch {name: 'Aerospace'})
        CREATE (rithvik)-[:STUDIES]->(:Branch {name: 'AI'})
        """
        session.run(query)
        print("Nodes, friendships, and additional relationships created successfully!")

# Execute the function
create_nodes_and_relationships()

driver.close()
