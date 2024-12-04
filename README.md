# Calculadora API

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/MyTruQs/calculator-design-patterns/blob/master/LICENSE)

# Sobre o projeto
Este projeto é uma API de calculadora construída com Flask. A API fornece quatro calculadoras diferentes, cada uma com funcionalidades específicas. A API também inclui tratamento de erros e testes automatizados.

## Rotas

A API possui as seguintes rotas:

### Calculadora 1
- **Rota:** `/calculator/1`
- **Método:** `POST`
- **Descrição:** Recebe um número, divide em três partes e realiza cálculos específicos em cada parte.
- **Exemplo de corpo da requisição:**
    ```json
    {
        "number": 10
    }
    ```
- **Exemplo de resposta:**
    ```json
    {
        "data": {
            "Calculator": 1,
            "result": 22.67
        }
    }
    ```

### Calculadora 2
- **Rota:** `/calculator/2`
- **Método:** `POST`
- **Descrição:** Recebe uma lista de números, multiplica cada número por 11, eleva a 0.95 e retorna o inverso do desvio padrão.
- **Exemplo de corpo da requisição:**
    ```json
    {
        "numbers": [2.12, 4.62, 1.32]
    }
    ```
- **Exemplo de resposta:**
    ```json
    {
        "data": {
            "Calculator": 2,
            "result": 0.33
        }
    }
    ```

### Calculadora 3
- **Rota:** `/calculator/3`
- **Método:** `POST`
- **Descrição:** Recebe uma lista de números, calcula a variância e a multiplicação dos números e verifica se a variância é menor que a multiplicação.
- **Exemplo de corpo da requisição:**
    ```json
    {
        "numbers": [1, 1, 1, 1, 100]
    }
    ```
- **Exemplo de resposta:**
    ```json
    {
        "data": {
            "Calculator": 3,
            "variance": 1000000,
            "multiplication": 100,
            "Success": True
        }
    }
    ```

### Calculadora 4
- **Rota:** `/calculator/4`
- **Método:** `POST`
- **Descrição:** Recebe uma lista de números e retorna a média dos números.
- **Exemplo de corpo da requisição:**
    ```json
    {
        "numbers": [1, 2, 3, 4, 5]
    }
    ```
- **Exemplo de resposta:**
    ```json
    {
        "data": {
            "Calculator": 4,
            "average": 3
        }
    }
    ```
    
## Instalação

Para instalar e executar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/MyTruQs/calculator-design-patterns.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd calculator-design-patterns
    ```
3. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```
4. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Execute a aplicação:
    ```bash
    python run.py
    ```

## Testes

Para executar os testes automatizados, utilize o comando:
```bash
pytest
```