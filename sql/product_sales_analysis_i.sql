/* https://leetcode.com/problems/product-sales-analysis-i/ */

SELECT p.product_name AS product_name,
s.year AS year,
s.price AS price
FROM Sales s LEFT JOIN Product p
ON s.product_id = p.product_id;
