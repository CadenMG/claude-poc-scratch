-- Speed up the inactive-users report.
ALTER TABLE users MODIFY COLUMN last_login_at DATETIME NOT NULL;
CREATE INDEX idx_users_last_login_at ON users (last_login_at);
