-- list all shows from the hbtn_0d_tvshows_rate database by their rating sum
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
