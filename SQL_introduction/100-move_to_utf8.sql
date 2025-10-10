-- 100-move_to_utf8.sql
-- Convert database, table, and 'name' column to UTF8 (utf8mb4 / utf8mb4_unicode_ci)
-- IMPORTANT: Do NOT set CHARACTER SET on the column; only set COLLATE.

-- 1) Set database defaults
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2) Work inside the DB
USE hbtn_0c_0;

-- 3) Convert the entire table to utf8mb4/unicode_ci
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 4) Ensure the column explicitly uses the unicode_ci collation
--    WITHOUT specifying CHARACTER SET, so it inherits from the table.
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  COLLATE utf8mb4_unicode_ci
  DEFAULT NULL;

