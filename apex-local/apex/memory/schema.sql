CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, namespace TEXT NOT NULL, content TEXT NOT NULL, metadata TEXT, created_at REAL NOT NULL);
CREATE INDEX IF NOT EXISTS idx_memory_namespace ON memory(namespace);
