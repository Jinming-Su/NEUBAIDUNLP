from neo4j import GraphDatabase
 
# Create db
db = GraphDatabase('/home/sujinming/Documents/software/neo4j-community-2.3.3/data/test')

# with db.transaction:
# db.node(name='sjming', age=42)

result = db.query("start n=node(1) return n.name")
print result

# Always shut down your database
db.shutdown()