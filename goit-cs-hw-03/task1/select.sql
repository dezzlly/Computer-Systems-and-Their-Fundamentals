--1
SELECT * FROM tasks WHERE user_id = 1;

--2
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

--3
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 5;

--4
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

--5
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Новий таск', 'Опис таску', (SELECT id FROM status WHERE name = 'new'), 2);

--6
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

--7
DELETE FROM tasks WHERE id = 3;

--8
SELECT * FROM users WHERE email LIKE '%@gmail.com';

--9
UPDATE users SET fullname = 'Оновлене Ім’я' WHERE id = 1;

--10
SELECT s.name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

--11
SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

--12
SELECT * FROM tasks WHERE description IS NULL;

--13
SELECT u.fullname, t.title FROM users u
JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

--14
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname;