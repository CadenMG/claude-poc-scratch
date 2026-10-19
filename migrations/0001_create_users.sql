-- Applied in production. The users table holds every account (about 2M rows)
-- and is written on every login by the reporting service.
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  last_login_at DATETIME NULL
) ENGINE=InnoDB;
