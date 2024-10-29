SELECT
  LEAST(u1.user_name, u2.user_name) AS u1_name,
  GREATEST(u1.user_name, u2.user_name) AS u2_name
FROM
  followers f
  JOIN users u1 ON f.user_id_fk = u1.user_id
  JOIN users u2 ON f.following_user_id_fk = u2.user_id
WHERE
  (u1.user_id, u2.user_id) IN (
    SELECT
      user_id_fk AS user_id1,
      following_user_id_fk AS user_id2
    FROM
      followers
    
    UNION ALL
    
    SELECT
      following_user_id_fk AS user_id1,
      user_id_fk AS user_id2
    FROM
      followers
  )
  AND u1.posts < u2.posts
ORDER BY
  u1.user_id;

/*
WITH mutual_followers AS (
  SELECT
    followers1.user_id_fk AS follower_id,
    followers1.following_user_id_fk AS following_id
  FROM followers followers1
  INNER JOIN followers followers2 ON followers1.user_id_fk = followers2.following_user_id_fk AND followers1.following_user_id_fk = followers2.user_id_fk
)

SELECT
  users1.user_name AS u1_name,
  users2.user_name AS u2_name
FROM mutual_followers
INNER JOIN users users1 ON mutual_followers.follower_id = users1.user_id
INNER JOIN users users2 ON mutual_followers.following_id = users2.user_id
WHERE users1.posts < users2.posts
ORDER BY users1.user_id;
*/
/*
WITH mutual_followers AS (
  SELECT
    followers1.user_id_fk AS follower_id,
    followers1.following_user_id_fk AS following_id
  FROM followers followers1
  INNER JOIN followers followers2 
    ON followers1.user_id_fk = followers2.following_user_id_fk 
    AND followers1.following_user_id_fk = followers2.user_id_fk
)

SELECT
  LEAST(users1.user_name, users2.user_name) AS u1_name,
  GREATEST(users1.user_name, users2.user_name) AS u2_name
FROM mutual_followers
INNER JOIN users users1 ON mutual_followers.follower_id = users1.user_id
INNER JOIN users users2 ON mutual_followers.following_id = users2.user_id
WHERE users1.posts < users2.posts
ORDER BY users1.user_id;
*/