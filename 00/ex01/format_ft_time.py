# format_ft_time.py
import time
from datetime import datetime

# Obter o tempo atual em segundos desde 01/01/1970 (época)
current_time_seconds = time.time()

# Formatar o tempo em notação científica
scientific_notation = "{:.4e}".format(current_time_seconds)

# Obter a data atual
current_date = datetime.now().strftime("%b %d %Y")

# Imprimir os resultados
print(f"Seconds since January 1, 1970: {current_time_seconds:.4f} or {scientific_notation} in scientific notation$")
print(current_date)