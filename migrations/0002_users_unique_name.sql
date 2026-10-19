-- Usernames are now unique so profiles can use them in URLs.
ALTER TABLE users ADD UNIQUE INDEX idx_users_name (name);
