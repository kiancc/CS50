SELECT title FROM movies
INNER JOIN stars ON movies.id = stars.movie_id
INNER JOIN people ON people.id = stars.person_id
WHERE name IN ('Johnny Depp', 'Helena Bonham Carter')
GROUP BY title
HAVING COUNT(DISTINCT name) = 2;