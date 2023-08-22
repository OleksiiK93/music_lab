DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    -- artist_id INT NOT NULL REFERENCES artists(id),
    artist VARCHAR(255),
    genre VARCHAR(255)
);

INSERT INTO albums (title, artist, genre) 
VALUES ('Marshall Mathers LP', 'Eminem', 'Hip-hop');
INSERT INTO albums (title, artist, genre)
VALUES ('Five', 'Five', 'Pop');