SELECT DISTINCT(name)
FROM stars
INNER JOIN people ON stars.person_id = people.id
WHERE movie_id IN (
    SELECT movie_id FROM movies
    INNER JOIN stars ON stars.movie_id = movies.id
    INNER JOIN people ON people.id = stars.person_id
    WHERE name IS 'Kevin Bacon' AND birth IS 1958
) AND name IS NOT 'Kevin Bacon';




