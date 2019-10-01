ALTER TABLE product ADD CONSTRAINT fk_product_categ_id FOREIGN KEY (categ_id) REFERENCES category(id);
