-- San pham co doanh so cao nhat trong thang 11/2017
SELECT product_id, 
     sum(qty*price_unit-amount_promotion) as revenue 
from sale_orderline
    JOIN sale_order ON sale_orderline.order_id=sale_order.id
WHERE date_order BETWEEN '2017-11-01' AND '2017-12-01'
group by product_id
order by revenue desc limit 10;

-- Nguoi mua hang(tien) nhieu nhat trong thang 11/2017
SELECT partner_id, 
     sum(qty*price_unit-amount_promotion) as revenue 
from sale_orderline
    JOIN sale_order ON sale_orderline.order_id=sale_order.id
WHERE date_order BETWEEN '2017-11-01' AND '2017-12-01'
group by partner_id
order by revenue desc limit 10;
