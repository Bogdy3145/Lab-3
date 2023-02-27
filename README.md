# Lab 3 assignment

**Points**: 1

**Deadline**: Week 4

**Last chance deadline and penalties**: Week 6, -0.3 points / week delayed

----

Continue working on the application from the previous assignment. Push your project to this repository.

You will need to:
- Add a **many to many** relation between `2` entities. This should be added as a separate entity containing the two related entities or their IDs and at least 2 additional attributes. For example: `Transaction` with `Product` and `Client` as the related entities and `Date` and `Volume` as the additional attributes.
- Make sure all of your entities are part of a `1 to 1`, `1 to many` or `many to many` relation.
- Add CRUD for all entities.
- Add a statistical report involving two entities. For example: show all movies ordered by the average age of their actors.

You are not allowed to write any raw SQL queries: it must all be done through an ORM.
