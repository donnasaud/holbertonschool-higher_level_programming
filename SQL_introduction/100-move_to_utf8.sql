-- 100-move_to_utf8.sql
-- Convert database, table, and 'name' column to UTF8 (utf8mb4 / utf8mb4_unicode_ci)
-- Ensure the 'name' column DOES NOT show 'CHARACTER SET' in SHOW CREATE TABLE.

-- 1) Set database defaults
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2) Use the database
USE hbtn_0c_0;

-- 3) Convert the whole table to utf8mb4/unicode_ci
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 4) Re-define the column WITHOUT specifying CHARACTER SET, only COLLATE
--    Using CHANGE (name appears twice) clears any explicit charset on the column.
ALTER TABLE first_table
  CHANGE name name VARCHAR(256)
  COLLATE utf8mb4_unicode_ci
  DEFAULT NULL;
