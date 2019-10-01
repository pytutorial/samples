CREATE TABLE category(
    id BIGINT NOT NULL AUTO_INCREMENT,
    parent_id BIGINT,
    name VARCHAR(200),
    PRIMARY KEY(id)) 
DEFAULT CHARACTER SET=utf8;

CREATE TABLE product(
    id BIGINT NOT NULL AUTO_INCREMENT,
    categ_id BIGINT,
    name VARCHAR(200),
	list_price DECIMAL,
    PRIMARY KEY(id)) 
DEFAULT CHARACTER SET=utf8;

ALTER TABLE product ADD CONSTRAINT fk_product_categ_id FOREIGN KEY (categ_id) REFERENCES category(id);
