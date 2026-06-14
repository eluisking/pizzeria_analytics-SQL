import pandas as pd

# 1. Cargar el archivo
df = pd.read_csv('C:/Users/luiss/Documents/Projects/pizzeria_analytics-SQL/DATA/pizza_sales.csv')

# 2. Transformar la columna de la fecha
# pd.to_datetime() lee el texto y lo convierte a un objeto de fecha.
# dt.strftime('%Y-%m-%d') le da el formato exacto que SQL necesita.
# Usamos dayfirst=True asumiendo que el formato original es Día/Mes/Año.
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True).dt.strftime('%Y-%m-%d')

# 3. Guardar el resultado en un nuevo archivo
nombre_nuevo_archivo = 'pizza_sales_sql_ready.csv'
df.to_csv(nombre_nuevo_archivo, index=False)

print(f"Transformación exitosa. Tu archivo {nombre_nuevo_archivo} está listo!.")