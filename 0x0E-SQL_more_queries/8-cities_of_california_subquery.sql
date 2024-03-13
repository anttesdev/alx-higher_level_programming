-- Retrieve all cities of California from the database hbtn_0d_usa, sorted by cities.id
USE hbtn_0d_usa;
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
