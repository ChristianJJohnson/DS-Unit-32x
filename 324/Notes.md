# ACID and Database Scalability Trade-offs

## At the end of this module, you should be able to:
understand and explain the advantages and disadvantages of traditional SQL databases
make informed decisions about alternative databases

## Definitions

* ACID - an acronym that helps the fundamental principles of a transnational system. ACID stands for Atomic, Consistent, Isolation, and Durability.
- Atomic – In a interaction involving two or more pieces of data, either all or none of the data is saved. (All or Nothing)
- Consistent – The saved data cannot mess up the structure of the database. Failed changes are rolled back to ensure the database is in a state before the change took place.
- Isolation – No interaction can affect the interaction in progress and must wait it's turn.   (No mid-air collisions)
- Durable –   Once a interaction is saved, it will remain so, regardless of a subsequent system failure.