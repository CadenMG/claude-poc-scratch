-- Profiles use a unique handle in their URL.
ALTER TABLE users ADD COLUMN handle VARCHAR(64) NOT NULL;
CREATE UNIQUE INDEX idx_users_handle ON users (handle);
