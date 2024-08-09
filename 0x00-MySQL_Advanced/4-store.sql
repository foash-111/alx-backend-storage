-- create trigger

CREATE TRIGGER follow_up
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
