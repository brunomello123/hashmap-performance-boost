Python Example: Performance Comparison Between O(N) and O(1)
Este projeto demonstra a diferença de performance entre duas abordagens de busca em listas e dicionários no Python.

Objetivo
O objetivo deste projeto é comparar o tempo de execução de uma busca linear em uma lista (O(N)) contra uma busca otimizada em um dicionário (O(1)), utilizando um exemplo com grandes quantidades de dados (1.000.000 departamentos).

Estrutura do Projeto
main.py: Arquivo principal que contém a implementação da comparação de desempenho.
Geração de dados de exemplo (10.000.000 departamentos e funcionários).
Implementação de duas funções de busca:
  get_employees_on(department): Busca linear em uma lista de tuplas (O(N)).
  get_employees_o1(department): Busca otimizada usando dicionário (O(1)).

Medição do tempo de execução das duas abordagens.

Como Rodar o Projeto
Clone este repositório para o seu ambiente local:

git clone https://github.com/seu-usuario/python-example.git
cd PythonExample
Instale o Python 3.11 (ou versão superior), se ainda não o tiver:

# Verifique se o Python está instalado
python --version
Execute o script main.py para observar a comparação de desempenho:

python main.py
O programa imprimirá o tempo de execução de cada abordagem no console:

Tempo O(N) (Busca em lista)
Tempo O(1) (Busca otimizada com dicionário)
