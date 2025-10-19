-- Database schema for Willr blog application
-- Defines the structure for user accounts and blog posts with proper relationships

-- Drop existing tables if they exist to ensure clean initialization
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- User table stores account information for authentication
-- Each user can create multiple blog posts
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

-- Post table stores blog posts with author attribution
-- Each post must be associated with a valid user (author)
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
