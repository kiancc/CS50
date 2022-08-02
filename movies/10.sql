SELECT name FROM ratings
INNER JOIN movies ON movies.id = ratings.movie_id
INNER JOIN directors ON directors.movie_id = movies.id
INNER JOIN people ON directors.person_id = people.id
WHERE rating >= 9.0;






/*
SELECT COUNT(DISTINCT(name)) FROM people
INNER JOIN directors ON people.id = directors.person_id
INNER JOIN ratings ON ratings.movie_id = directors.movie_id
WHERE rating >= 9.0;*/