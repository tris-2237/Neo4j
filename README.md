# Using Neo4j Aura to Simulate Large-Scale Relationship Data

This repository documents my hands-on experience using [Neo4j AuraDB Free](https://neo4j.com/cloud/aura/) to build and analyze a graph database with **10,000+ relationships**. It was created to explore how Neo4j handles real-world graph problems efficiently and intuitively.

## 🔍 Problem

In many real-life systems — like e-commerce, social media, or recommender systems — relationships between entities are as important as the entities themselves. I wanted to test how a graph database handles high-volume, dense relationships like **"User BOUGHT Product"**.

## 🧪 What I Did

- Created a Neo4j Aura Free instance (`b28b9b15`)
- Generated 100 `User` and 100 `Product` nodes
- Programmatically created **10,000 `BOUGHT` relationships** between them
- Queried, visualized, and analyzed the network using Cypher

## 🧠 Key Learnings

- **Cypher queries** are very expressive and fast for relationship-centric problems.
- Neo4j Aura handles complex graph structures **surprisingly well**, even on the free tier.
- Perfect for **prototyping** relationship-heavy use cases.

## 🧾 Sample Query

```cypher
MATCH (u:User)-[:BOUGHT]->(p:Product)
RETURN u.id AS User, COUNT(p) AS ProductsBought
ORDER BY ProductsBought DESC
LIMIT 10;

## 🙌 Why I Recommend Neo4j

Neo4j made it easy to:
<ul>
<li>Scale test data quickly

<li>Visualize graph structures

<li>Learn graph-based thinking
</ul>
