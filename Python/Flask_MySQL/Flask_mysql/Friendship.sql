SELECT user.first_name, user.last_name, user2.first_name, user2.first_name FROM user
LEFT JOIN friendships ON friendships.user_id = user.id
LEFT JOIN user AS user2 ON  user2.id = friendships.id;