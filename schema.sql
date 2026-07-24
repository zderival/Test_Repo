CREATE TABLE IF NOT EXISTS "user"(id uuid PRIMARY KEY, username VARCHAR(32),email VARCHAR(255), password TEXT,dob DATE, created_at TIMESTAMP);
CREATE TABLE IF NOT EXISTS user_prefrences(id UUID PRIMARY KEY, user_id UUID REFERENCES "user"(id) ON DELETE CASCADE, topic TEXT);
CREATE TABLE IF NOT EXISTS saved_article( id UUID PRIMARY KEY, user_id UUID REFERENCES "user"(id) ON DELETE CASCADE, title TEXT, source TEXT, url TEXT, UNIQUE (user_id,url));
CREATE TABLE IF NOT EXISTS read_articles(id UUID PRIMARY KEY, user_id UUID REFERENCES "user"(id) ON DELETE CASCADE, source TEXT, url TEXT, read_at TIMESTAMP);
CREATE TABLE IF NOT EXISTS search_history(id UUID PRIMARY KEY, user_id UUID REFERENCES "user"(id) ON DELETE CASCADE, keyword TEXT, searched_at TIMESTAMP);
