ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modify List
ft_list[1] = "World!"

# Modify Tuple
new_tuple = list(ft_tuple)
new_tuple.remove("toto!")
ft_tuple = tuple(new_tuple)
country = ("Portugal!",)
ft_tuple += country

# Modify Set
ft_set.remove("tutu!")
ft_set.add("Lisbon!")

# Modify Dict
ft_dict["Hello"] = "42Lisbon!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

"""
Lista: Ordenada, mutável, elementos acessados por índices.
Tupla: Ordenada, imutável.
Conjunto: Não ordenado, elementos únicos.
Dicionário: Não ordenado, acessado por chaves únicas.
"""
