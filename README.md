# curso-python 🐍

Repositório de estudos práticos em Python, organizado por fases progressivas.  
Criado como parte da minha preparação para o estágio em **QA e Automação de Testes**.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Em_andamento-yellow?style=flat-square)]()
[![UEA](https://img.shields.io/badge/UEA-Sistemas_de_Informação-orange?style=flat-square)](https://uea.edu.br)

---

## Sobre este repositório

Este repositório documenta minha evolução prática em Python, do zero até os fundamentos necessários para automação de testes e computação visual. Cada módulo contém exercícios comentados, exemplos funcionais e um desafio integrador.

O objetivo não é só aprender — é registrar o processo de aprendizado de forma transparente.

---

## Estrutura

```
curso-python/
│   README.md
│
└───fase-1/                          ← Fundamentos de Python
    │
    ├───exercicio/                   ← Exercícios práticos por conta própria
    │       exercicio001.py
    │       exercicio002.py
    │
    └───modulo-01/                   ← Aulas organizadas por tema
        │
        ├───variaveis/
        │       aula001.py
        │       aula002.py
        │       aula003.py
        │       aula004.py
        │       aula005.py
        │
        ├───tipos/
        │       aula001.py
        │
        └───operadores/
```

---

## Fase 1 — Fundamentos de Python

| # | Módulo | Conceitos praticados |
|---|--------|----------------------|
| 01 | Variáveis, Tipos e Operadores | `int`, `float`, `str`, `bool`, operadores aritméticos, comparação e lógicos, `type()`, conversão de tipos |
| 02 | Condicionais e Loops | `if/elif/else`, `while`, `for`, `break`, `continue`, loops aninhados, FizzBuzz |
| 03 | Funções e Escopo | `def`, `return`, parâmetros padrão, múltiplos retornos, escopo local/global, recursão, docstrings |
| 04 | Listas, Dicionários e Tuplas | Métodos de lista, list comprehension, dicionários, tuplas, estruturas combinadas |
| 05 | Leitura e Escrita de Arquivos | `open()`, modos `r/w/a`, `with`, `.txt`, `.csv`, tratamento de `FileNotFoundError` |

Cada arquivo segue a mesma estrutura interna:

```
Exercício 1 — conceito introdutório
Exercício 2 — variação ou aprofundamento
...
Exercício N — consolidação
Desafio     — problema que integra os conceitos do módulo
```

---

## Como executar

**Pré-requisito:** Python 3.10 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/DanielNazarioPro/curso-python.git
cd curso-python

# Execute uma aula
python fase-1/modulo-01/variaveis/aula001.py
python fase-1/modulo-01/tipos/aula001.py

# Execute um exercício
python fase-1/exercicio/exercicio001.py
```

> Os módulos 03, 04 e 05 não precisam de bibliotecas externas — apenas Python padrão.  
> O módulo 05 cria uma pasta `arquivos_gerados/` no diretório onde for executado.

---

## Progresso

- [x] Fase 1 — Fundamentos de Python
- [ ] Fase 2 — Qualidade de software e pytest
- [ ] Fase 3 — Automação de testes (Selenium, requests)
- [ ] Fase 4 — Computação visual com OpenCV

---

## Por que estou estudando isso?

Estou me preparando para uma vaga de **Estagiário de QA – Automação de Testes**, que exige:

- Escrita de scripts de automação em Python
- Execução e análise de testes automatizados
- Validação de imagens com técnicas de computação visual

Este repositório é a prova prática do meu processo de aprendizado.

---

## Autor

**Daniel Nazário** — Estudante de Sistemas de Informação, UEA, Manaus-AM  
[LinkedIn](https://linkedin.com/in/danielnazariopro/) · [GitHub](https://github.com/DanielNazarioPro)