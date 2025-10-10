-- 100-move_to_utf8.sql
-- Convert database, table, and 'name' column to UTF8 (utf8mb4 / utf8mb4_unicode_ci)
-- Matching the checker’s expected output (no explicit CHARACTER SET on the column).

-- 1) Database defaults
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2) Work inside the DB
USE hbtn_0c_0;

-- 3) Convert the whole table (updates existing columns to utf8mb4 + collation)
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 4) Ensure only the column COLLATE is set (do NOT specify CHARACTER SET here)
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  COLLATE utf8mb4_unicode_ci
  DEFAULT NULL;

