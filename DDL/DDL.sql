-- Creamos la base de datos específica para este proyecto
CREATE DATABASE pizzeria_analytics;

-- Le indicamos al gestor que use esta nueva base de datos
USE pizzeria_analytics;

-- Creamos la tabla plana con los tipos de datos correctos
CREATE TABLE ventas_pizza (
    pizza_id INT PRIMARY KEY,
    order_id INT,
    pizza_name_id VARCHAR(50),
    quantity INT,
    order_date DATE,
    order_time TIME,
    unit_price DECIMAL(5,2),
    total_price DECIMAL(5,2),
    pizza_size VARCHAR(5),
    pizza_category VARCHAR(50),
    pizza_ingredients TEXT,
    pizza_name VARCHAR(100)
);