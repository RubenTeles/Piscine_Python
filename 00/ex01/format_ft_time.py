from datetime import datetime

# Seconds since January 1, 1970: 1,666,355,857.3622
# or 1.67e+09 in scientific notation$

first_date = datetime(1970, 1, 1)
current_date = datetime.now()

seconds = (current_date - first_date).total_seconds()
scientific_notation = "{:e}".format(seconds)

# NOV 27 2023
format_date = "%b %d %Y"
string_date = "Seconds since January 1, 1970:"
string_date_end = " in scientific notation"

print(string_date, seconds, "or", scientific_notation, string_date_end)
print(current_date.strftime(format_date))

# %Y: Ano com quatro dígitos (ex: 2023).
# %m: Mês como número decimal com zero à esquerda (01 a 12).
# %d: Dia do mês como número decimal com zero à esquerda (01 a 31).
# %H: Hora (00 a 23).
# %M: Minutos (00 a 59).
# %S: Segundos (00 a 59).
# %a: Abreviação do nome do dia da semana (Sun, Mon, Tue, etc.).
# %A: Nome completo do dia da semana
# (Sunday, Monday, Tuesday, etc.).
# %b: Abreviação do nome do mês (Jan, Feb, Mar, etc.).
# %B: Nome completo do mês (January, February, March, etc.).
