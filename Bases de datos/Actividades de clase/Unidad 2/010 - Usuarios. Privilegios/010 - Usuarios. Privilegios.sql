sudo mysql -u root -p

SELECT User, Host FROM mysql.user;

CREATE USER 'anasanchez'@'localhost' IDENTIFIED BY 'sogtulapdt';

SELECT User, Host FROM mysql.user;

GRANT ALL PRIVILEGES ON *.* TO 'anasanchez'@'localhost';

FLUSH PRIVILEGES;
