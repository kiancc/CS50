SELECT title FROM people
INNER JOIN stars ON stars.person_id = people.id
INNER JOIN movies ON stars.movie_id = movies.id
INNER JOIN ratings ON movies.id = ratings.movie_id
WHERE name = 'Chadwick Boseman'
ORDER BY rating DESC
LIMIT 5;