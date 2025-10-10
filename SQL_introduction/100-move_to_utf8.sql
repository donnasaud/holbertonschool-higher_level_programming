-- 100-move_to_utf8.sql
-- Convert database, table, and column to UTF8 (utf8mb4 / utf8mb4_unicode_ci)

-- 1) Database default charset/collation
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2) Make sure we’re operating inside the target DB
USE hbtn_0c_0;

-- 3) Convert the whole table (structure + existing data)
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 4) Ensure the 'name' column is explicitly utf8mb4/utf8mb4_unicode_ci
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

