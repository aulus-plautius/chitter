DROP TABLE IF EXISTS peeps CASCADE;
-- Create the first table.
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content text,
  name text,
  handle text,
  time timestamp
);


DROP TABLE IF EXISTS users CASCADE;
-- Create the second table.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text,
  name text,
  handle text
);

DROP TABLE IF EXISTS peeps_users;
-- Create the join table.
CREATE TABLE peeps_users (
  peep_id int,
  user_id int,
  constraint fk_peep foreign key(peep_id) references peeps(id) on delete cascade,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade,
  PRIMARY KEY (peep_id, user_id)
);

-- SEED DATA - users
INSERT INTO users (email, password, name, handle) VALUES 
('john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe'),
('jane.smith@example.com', 'Jane#4567', 'Jane Smith', '@jane_smith'),
('mike.johnson@example.com', 'Mike@7890', 'Mike Johnson', '@mike_j'),
('sarah.davis@example.com', 'Sarah!8765', 'Sarah Davis', '@sarah_d');

-- SEED DATA - peeps
INSERT INTO peeps (content, name, handle, time) VALUES 
('Just finished a great workout!', 'John Doe', '@john_doe', '2024-08-22 08:00'),
('Loving this sunny weather.', 'Jane Smith', '@jane_smith', '2024-08-22 12:30'),
('Reading a fantastic book right now.', 'Mike Johnson', '@mike_j', '2024-08-21 19:00'),
('Coffee always makes the day better.', 'Emily Brown', '@emily_b', '2024-08-21 09:45'),
('Excited for the weekend ahead.', 'David Wilson', '@david_w', '2024-08-22 10:15'),
('Had a great time exploring the city.', 'Sarah Davis', '@sarah_d', '2024-08-22 16:00'),
('Trying out a new recipe tonight.', 'John Doe', '@john_doe', '2024-08-20 18:30'),
('Just baked some fresh cookies.', 'Sarah Davis', '@sarah_d', '2024-08-22 15:30');

-- SEED DATA - peeps_users
INSERT INTO peeps_users (peep_id, user_id) VALUES
(3, 1),
(5, 1),
(6, 1),
(7, 2),
(8, 2),
(2, 3),
(4, 3),
(6, 3),
(1, 3),
(1, 4),
(5, 4),
(8, 4);



