-- import DB
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
INNER JOIN tv_shows s ON s.id = sg.show_id
GROUP BY g.id, g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
