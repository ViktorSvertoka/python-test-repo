MERGE INTO products
    (title, price)
    KEY (title)
    VALUES ('Sugar', 32.0),
           ('Salt', 19.0),
           ('Bread', 20.0),
           ('Butter', 62.0),
           ('Milk', 32.0);
