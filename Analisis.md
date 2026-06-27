# pizzeria_analytics-SQL  

Cree algunas preguntas com inteligencia artificial, la cual esta pensando como el dueño de negocio, este nos dira preguntas que nosotros tenemos que resolver con SQL. Vamos alla!!

## 1 - Un vistazo al menu.
Dev, necesito revisar rápido cómo está estructurado nuestro menú en el sistema. Tráeme un reporte que muestre únicamente el nombre de la pizza, la categoría a la que pertenece y su tamaño.

Ojo, no quiero que la pantalla se me llene con miles de filas porque me mareo, muéstrame solo los primeros 15 registros. Además, asegúrate de que los encabezados de las columnas sean limpios y en español para que yo los entienda rápido.

```sql
SELECT DISTINCT pizza_name AS Nombre,
	   pizza_category AS Categoria,
       pizza_size AS Tamaño
FROM ventas_pizza
ORDER by Nombre, Tamaño
LIMIT 15;
```

## 2 - Un día de locos.
Dev, el Día de San Valentín siempre es un caos en la cocina y quiero saber qué tan pesado estuvo el turno. Necesito que me digas cuántas pizzas en total (la suma de las cantidades, no el dinero) salieron de nuestros hornos exactamente el 14 de febrero de 2015.

Entrégame un solo número, y ponle a esa columna el alias Total_Pizzas_San_Valentin.

```sql
SELECT SUM(quantity) AS Total_de_ventas_san_valentin
FROM ventas_pizza
WHERE order_date = '2015-02-14';
```

## 3 - ¿Dónde está el dinero?
Devs, necesito saber qué sección de nuestro menú es la que realmente mantiene a flote este negocio. Prepárame un reporte que me muestre la categoría de la pizza (Classic, Supreme, Veggie, Chicken) y al lado, el dinero total (ingresos) que nos ha generado cada una a lo largo de toda nuestra historia. Además, para no tener que estar buscando, ordénalo de mayor a menor ingreso, dejando a la categoría más rentable hasta arriba.

```sql
SELECT pizza_category AS Categoria,
	   SUM(total_price) AS Total_ingreso
FROM ventas_pizza
GROUP BY pizza_category
ORDER BY Total_ingreso DESC;
```

## 4 - Los consentidos de la casa.
Dev, estoy armando la estrategia de marketing para el próximo mes y quiero meterle presupuesto a las pizzas que la gente ya ama. Necesito que me saques un reporte con las 5 pizzas más vendidas de toda nuestra historia (por su nombre exacto, pizza_name).

Quiero ver el nombre de la pizza y la cantidad total de unidades que se han preparado de cada una. Ordénalo de la más vendida a la menos vendida de ese grupo.

```sql
SELECT pizza_name AS Nombre_pizza,
       sum(quantity) AS Total_de_ventas
FROM ventas_pizza
GROUP BY Nombre_pizza
ORDER BY Total_de_ventas DESC
LIMIT 5;
```