SELECT product_id, sum(qty) as total from sale_orderline
    JOIN sale_order ON sale_orderline.order_id=sale_order.id
WHERE date_order BETWEEN '2017-11-01' AND '2017-11-02'
group by product_id
order by total desc limit 10
