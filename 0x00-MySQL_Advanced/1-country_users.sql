-- Write a SQL script that creates a table users following these requirements:

-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
-- If the table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS `users` (
    `id` int NOT NULL UNIQUE,
    `email` varchar(255) NOT NULL UNIQUE,
    `name` varchar(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

