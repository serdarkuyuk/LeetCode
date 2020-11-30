SELECT IFNULL(
        (ROUND(
            (SELECT COUNT(*)
            FROM (  SELECT COUNT(*)
                    FROM RequestAccepted
                    GROUP BY requester_id, accepter_id) AS Accepted) /
            (SELECT COUNT(*)
            FROM (  SELECT COUNT(*)
                    FROM FriendRequest
                    GROUP BY sender_id, send_to_id) AS Request), 2)), 0)
            AS accept_rate
