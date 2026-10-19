-- Store a login email for every user and look users up by it.
ALTER TABLE users ADD COLUMN email VARCHAR(255) NOT NULL;
CREATE UNIQUE INDEX idx_users_email ON users (email);
