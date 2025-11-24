import json
from typing import List, Dict, Union

# Questão 08: Função para calcular o valor de impostos
def calcular_imposto(valor_produto: float) -> float:
    """
    Calcula o valor do imposto sobre o valor do produto com base nas regras:
    - > 3000: 18%
    - > 2000: 15%
    - < 2000 e >= 1000: 12%
    - < 1000: 0%
    """
    if valor_produto >= 3000:
        aliquota = 0.18
    elif valor_produto >= 2000:
        aliquota = 0.15
    elif valor_produto >= 1000:
        aliquota = 0.12
    else:
        aliquota = 0.0
    
    return valor_produto * aliquota

# Questão 09: Função para calcular o relatório de notas dos alunos
def gerar_relatorio_notas(notas: List[Union[int, float]]) -> Dict[str, Union[float, int, List[Union[int, float]]]]:
    """
    Gera um relatório de notas contendo:
    1. Média das notas.
    2. Maior nota.
    3. Menor nota.
    4. Lista de notas acima de 7 (aprovados).
    5. Quantidade de reprovados (nota < 5).
    6. Quantidade de recuperação (notas 5 e 6).
    """
    if not notas:
        return {
            "media": 0.0,
            "maior_nota": 0.0,
            "menor_nota": 0.0,
            "aprovados": [],
            "quantidade_reprovados": 0,
            "quantidade_recuperacao": 0
        }

    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    aprovados = [nota for nota in notas if nota > 7]
    quantidade_reprovados = sum(1 for nota in notas if nota < 5)
    quantidade_recuperacao = sum(1 for nota in notas if 5 <= nota <= 6)

    return {
        "media": round(media, 2),
        "maior_nota": maior_nota,
        "menor_nota": menor_nota,
        "aprovados": aprovados,
        "quantidade_reprovados": quantidade_reprovados,
        "quantidade_recuperacao": quantidade_recuperacao
    }

# Exemplo de uso para a Questão 08
valor_exemplo_q8 = 2500.00
imposto_q8 = calcular_imposto(valor_exemplo_q8)
resposta_q8 = f"O imposto para um produto de R$ {valor_exemplo_q8:.2f} é de R$ {imposto_q8:.2f} (15%)."

# Exemplo de uso para a Questão 09
notas_exemplo_q9 = [8, 7.5, 9, 6, 4, 10, 5]
relatorio_q9 = gerar_relatorio_notas(notas_exemplo_q9)
resposta_q9 = json.dumps(relatorio_q9, indent=4)

# Para fins de documentação no relatório final
resposta_q8_completa = f"""
Função em Python:
```python
{calcular_imposto.__doc__}
def calcular_imposto(valor_produto: float) -> float:
    if valor_produto >= 3000:
        aliquota = 0.18
    elif valor_produto >= 2000:
        aliquota = 0.15
    elif valor_produto >= 1000:
        aliquota = 0.12
    else:
        aliquota = 0.0
    
    return valor_produto * aliquota
```
Exemplo: Para R$ 2500.00, o imposto é de R$ {imposto_q8:.2f}.
"""

resposta_q9_completa = f"""
Função em Python:
```python
{gerar_relatorio_notas.__doc__}
def gerar_relatorio_notas(notas: List[Union[int, float]]) -> Dict[str, Union[float, int, List[Union[int, float]]]]:
    if not notas:
        # ... (código para lista vazia)
        pass

    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    aprovados = [nota for nota in notas if nota > 7]
    quantidade_reprovados = sum(1 for nota in notas if nota < 5)
    quantidade_recuperacao = sum(1 for nota in notas if 5 <= nota <= 6)

    return {{
        "media": round(media, 2),
        "maior_nota": maior_nota,
        "menor_nota": menor_nota,
        "aprovados": aprovados,
        "quantidade_reprovados": quantidade_reprovados,
        "quantidade_recuperacao": quantidade_recuperacao
    }}
```
Exemplo de entrada: {notas_exemplo_q9}
Relatório gerado:
{resposta_q9}
"""

# Salvar as respostas para uso posterior no JSON final
with open("resposta_q08.txt", "w") as f:
    f.write(resposta_q8_completa)

with open("resposta_q09.txt", "w") as f:
    f.write(resposta_q9_completa)
