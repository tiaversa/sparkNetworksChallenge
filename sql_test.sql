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
select'2021_11' col, ROUND(AVG(log_2021_11),2) value
from subscriptions
union all
select'2021_12' col, ROUND(AVG(log_2021_12),2) value
from subscriptions
union all
select'2022_01' col, ROUND(AVG(log_2022_01),2) value
from subscriptions
union all
select'2022_02' col, ROUND(AVG(log_2022_02),2) value
from subscriptions
union all
select'2022_03' col, ROUND(AVG(log_2022_03),2) value
from subscriptions
union all
select'2022_04' col, ROUND(AVG(log_2022_04),2) value
from subscriptions
union all
select'2022_05' col, ROUND(AVG(log_2022_05),2) value
from subscriptions
union all
select'2022_06' col, ROUND(AVG(log_2022_06),2) value
from subscriptions
union all
select'2022_07' col, ROUND(AVG(log_2022_07),2) value
from subscriptions
union all
select'2022_08' col, ROUND(AVG(log_2022_08),2) value
from subscriptions
union all
select'2022_09' col, ROUND(AVG(log_2022_09),2) value
from subscriptions
union all
select'2022_10' col, ROUND(AVG(log_2022_10),2) value
from subscriptions
union all
select'2022_11' col, ROUND(AVG(log_2022_11),2) value
from subscriptions;