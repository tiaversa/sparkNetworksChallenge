USE spark_networks_test;
-- How many total messages are being sent every day?
SELECT CAST(createdAt AS DATE) AS date_message_created, COUNT(*) AS total_messages_by_date
	FROM messages 
		GROUP BY CAST(createdAt AS DATE);
        
        
-- Are there any users that did not receive any message?
SELECT user_id AS user_without_messages
	FROM users u
		LEFT OUTER JOIN messages m ON u.user_id = m.receiverId
		WHERE m.receiverId IS NULL
		ORDER BY user_id;

-- How many active subscriptions do we have today?
SELECT COUNT(status_subscription) AS active_subscriptions 
	FROM subscriptions 
    WHERE status_subscription = 'Active';


-- How much is the average price ticket (sum amount subscriptions / count subscriptions) breakdown by year/month (format YYYY-MM)?
SELECT DATE_FORMAT(createdAt, '%M,%Y') as month, sum(amount)/ count(*) average_price
	FROM subscriptions
    GROUP BY DATE_FORMAT(createdAt, '%M,%Y')
    ORDER BY DATE_FORMAT(createdAt, '%M,%Y') ;