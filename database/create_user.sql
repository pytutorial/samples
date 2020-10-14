CREATE USER admin@localhost IDENTIFIED BY 'abc@123';
GRANT ALL ON *.* TO admin@localhost;
FLUSH PRIVILEGES;
