SELECT * FROM product where id=5251;
SELECT * FROM category where id=4741;

SELECT product.id, product.name_template as product, list_price, category.name as category 
    FROM product JOIN category ON product.categ_id=category.id 
WHERE product.id=5251;
