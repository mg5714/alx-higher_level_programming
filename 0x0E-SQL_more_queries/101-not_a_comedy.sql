--list all shows without the genre "Comedy" in the hbtn_0d_tvshows database
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
)
ORDER BY title ASC;
