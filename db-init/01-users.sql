




CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    joining_date DATE NOT NULL,
    is_registered TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id)
);