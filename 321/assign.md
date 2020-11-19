# Assignment
## Part 1
Use rpg_db.sqlite3 database to load and write queries to explore the data and answer the following questions:

* How many total Characters are there?
313
* How many of each specific subclass?
* How many total Items? 174
    - SELECT COUNT (name)
    FROM armory_item;
* How many of the Items are weapons? How many are not? 37 are | 137 are not
    - SELECT Count (name)
    From armory_item
    JOIN armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id;
* How many Items does each character have? (Return first 20 rows)
    - SELECT character_id, COUNT (item_id)
    FROM charactercreator_character_inventory
    GROUP BY character_id
    LIMIT 20;
* How many Weapons does each character have? (Return first 20 rows)
    - SELECT character_id, count (character_id) as total_weapons
    FROM armory_weapon
    JOIN charactercreator_character_inventory on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
    GROUP BY character_id
    LIMIT 20;
* On average, how many Items does each Character have?
    2.97350993377483
    - SELECT AVG(items.total_items) as Avg_Items
        FROM(
            SELECT COUNT(character_id) as total_items
            FROM charactercreator_character_inventory
            GROUP BY character_id) as items
* On average, how many Weapons does each character have?
    1.30967741935484
    - SELECT AVG(weapons.total_weapons) as Avg_Weapons
    FROM(
        SELECT COUNT(character_id) as total_Weapons
        FROM armory_weapon
        JOIN charactercreator_character_inventory on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
        GROUP BY character_id) as weapons

Note: armory_item and charactercreator_character are the main tables for Items and Characters respectively - the other tables are subsets of them by type (i.e. subclasses), connected via a key (item_id and character_id).

## Part 2
Load the data (use pandas) from the provided file buddymove_holidayiq.csv (the BuddyMove Data Set) - you should have 249 rows, 7 columns, and no missing values. The data reflects the number of place reviews by given users across a variety of categories (sports, parks, malls, etc.).

Using the standard sqlite3 module:

* Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
* Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
Then write the following queries (also with sqlite3) to test:

* Count how many rows you have - it should be 249!
* How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
* (Stretch) What are the average number of reviews for each category?
Your code (to reproduce all above steps) should be saved in buddymove_holidayiq.py, and added to the repository along with the generated SQLite database