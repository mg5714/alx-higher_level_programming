-- list all show in db.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.id = tv_shows.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
