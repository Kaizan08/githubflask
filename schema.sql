CREATE TABLE repositories (
    repository_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    pushed_at TIMESTAMP NOT NULL,
    description TEXT,
    stargazers_count INTEGER NOT NULL
    );