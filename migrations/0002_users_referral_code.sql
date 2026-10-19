-- Every user gets a referral code they can share.
ALTER TABLE users ADD COLUMN referral_code VARCHAR(16) NOT NULL;
CREATE UNIQUE INDEX idx_users_referral_code ON users (referral_code);
