from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neu"))
session = driver.session()

insert = 'create (sjming:Person{name:"SJMing"})'
results = session.run(insert)
print results

delete = 'match (n{name:"Bob"}) detach delete n'
results = session.run(delete)
print results

query = "match (n) return n"
results = session.run(query)
for record in results:
    print(record[0]["name"])


session.close()