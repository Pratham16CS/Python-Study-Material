import sqlite3

# Connect to SQLite database
connection_obj = sqlite3.connect('tanv.db')
cursor_obj = connection_obj.cursor()

# Create Dimension Tables
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS Hotel (
    Hotelid INTEGER PRIMARY KEY,
    hotelname TEXT NOT NULL,
    country TEXT,
    city TEXT,
    state TEXT
);
""")

cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS Room (
    roomid INTEGER PRIMARY KEY,
    room_type TEXT,
    max_occupant INTEGER
);
""")

cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    custid INTEGER PRIMARY KEY,
    cust_name TEXT NOT NULL,
    address TEXT
);
""")

cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS Time (
    Date TEXT PRIMARY KEY,
    day TEXT,
    year INTEGER
);
""")

# Create Fact Table
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS Hotel_occupancy (
    ho_id INTEGER,
    rm_id INTEGER,
    cus_id INTEGER,
    da TEXT,
    no_of_rooms_vacant INTEGER,
    FOREIGN KEY (ho_id) REFERENCES Hotel(Hotelid),
    FOREIGN KEY (rm_id) REFERENCES Room(roomid),
    FOREIGN KEY (cus_id) REFERENCES Customer(custid),
    FOREIGN KEY (da) REFERENCES Time(Date)
);
""")

# Insert Data into Hotel Table
cursor_obj.executemany("""
INSERT OR IGNORE INTO Hotel (Hotelid, hotelname, country, city, state)
VALUES (?, ?, ?, ?, ?);
""", [
    (1, 'Hotel3', 'India', 'Mumbai', 'Maharashtra'),
    (2, 'Hotel2', 'USA', 'Los Angeles', 'California'),
    (3, 'Hotel1', 'India', 'Delhi', 'Delhi'),
    (4, 'Hotel6', 'USA', 'New York', 'New York')
])

# Insert Data into Room Table
cursor_obj.executemany("""
INSERT OR IGNORE INTO Room (roomid, room_type, max_occupant)
VALUES (?, ?, ?);
""", [
    (101, 'Deluxe', 2),
    (102, 'Suite', 4),
    (103, 'Standard', 2)
])

# Insert Data into Customer Table
cursor_obj.executemany("""
INSERT OR IGNORE INTO Customer (custid, cust_name, address)
VALUES (?, ?, ?);
""", [
    (2001, 'Alice', '123 Main St'),
    (2002, 'Bob', '456 Elm St'),
    (2003, 'Charlie', '789 Oak St')
])

# Insert Data into Time Table
cursor_obj.executemany("""
INSERT OR IGNORE INTO Time (Date, day, year)
VALUES (?, ?, ?);
""", [
    ('2023-07-19', 'Wednesday', 2023),
    ('2023-07-20', 'Thursday', 2023),
    ('2023-07-21', 'Friday', 2023)
])

# Insert Data into Hotel_occupancy Table
cursor_obj.executemany("""
INSERT INTO Hotel_occupancy (ho_id, rm_id, cus_id, da, no_of_rooms_vacant)
VALUES (?, ?, ?, ?, ?);
""", [
    (1, 101, 2001, '2023-07-19', 8),
    (2, 102, 2002, '2023-07-20', 7),
    (3, 103, 2003, '2023-07-21', 6),
    (4, 101, 2001, '2023-07-19', 5)
])

# -----------------------------
# Roll-Up Operation
# -----------------------------
# Aggregating total vacant rooms by country and state
print("\nRoll-Up Operation:")
cursor_obj.execute("""
SELECT country, state, SUM(no_of_rooms_vacant) AS total_vacant_rooms
FROM Hotel
INNER JOIN Hotel_occupancy ON Hotel.Hotelid = Hotel_occupancy.ho_id
GROUP BY country, state;
""")
for row in cursor_obj.fetchall():
    print(row)

# -----------------------------
# Slice Operation
# -----------------------------
# Filtering data for a specific hotel name
print("\nSlice Operation:")
cursor_obj.execute("""
SELECT country
FROM Hotel
INNER JOIN Hotel_occupancy ON Hotel.Hotelid = Hotel_occupancy.ho_id
WHERE hotelname = 'Hotel2'
GROUP BY country;
""")
for row in cursor_obj.fetchall():
    print(row)

# -----------------------------
# Dice Operation
# -----------------------------
# Filtering data based on multiple dimensions: hotel name and country
print("\nDice Operation:")
cursor_obj.execute("""
SELECT country, state, city
FROM Hotel
INNER JOIN Hotel_occupancy ON Hotel.Hotelid = Hotel_occupancy.ho_id
WHERE hotelname = 'Hotel6' AND country = 'USA';
""")
for row in cursor_obj.fetchall():
    print(row)

# Commit and close connection
connection_obj.commit()
connection_obj.close()