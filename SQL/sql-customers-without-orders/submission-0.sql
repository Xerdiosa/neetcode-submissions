-- Write your query below
SELECT name FROM customers 
WHERE NOT EXISTS (
    SELECT 1 FROM orders WHERE customers.id = orders.customer_id
);