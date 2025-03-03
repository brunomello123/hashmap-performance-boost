import time

# Gerando lista de departamentos
data_size = 10000000
search_key = "Depto_500000"

departments = [(f"Depto_{i}", [f"Emp_{i}_1", f"Emp_{i}_2"]) for i in range(data_size)]

# Criando HashMap (dict)
department_map = {dept: employees for dept, employees in departments}

# O(N) – Busca ineficiente
def get_employees_on(department):
    return [employees for d, employees in departments if d == department][0] if department in dict(departments) else []

#O(1) – Busca otimizada
def get_employees_o1(department):
    return department_map.get(department, [])

# Medindo tempos
start = time.time()
get_employees_o1(search_key)
print(f"Tempo O(1): {round((time.time() - start) * 1000, 2)}ms")

start = time.time()
get_employees_on(search_key)
print(f"Tempo O(N): {round((time.time() - start) * 1000, 2)}ms")

