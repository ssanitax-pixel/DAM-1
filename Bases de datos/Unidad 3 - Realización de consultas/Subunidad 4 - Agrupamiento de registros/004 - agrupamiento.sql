SELECT COUNT(color)
FROM productos; -- resumen

SELECT COUNT(color),color
FROM productos
GROUP BY color; -- te dice cuantos hay de cada color
