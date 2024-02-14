--list all shows without the genre "Comedy" in the hbtn_0d_tvshows database
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
