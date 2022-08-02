
WITH temporary_id AS (
   SELECT id
   FROM artists
   WHERE name = 'Post Malone'
)
SELECT name
FROM temporary_id
JOIN songs
  ON temporary_id.id = songs.artist_id;

