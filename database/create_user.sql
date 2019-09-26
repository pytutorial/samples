CREATE USER test@localhost IDENTIFIED BY 'abc@123';
GRANT ALL ON *.* TO test@localhost;
FLUSH PRIVILEGES;