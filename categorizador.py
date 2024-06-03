from openai import OpenAI
from dotenv import load_dotenv
import os

#lê do arquivo .env a chave do GPT
load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.

            # Lista de Categorias Válidas
            {lista_categorias_possiveis.split(",")}

            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
        """

#    prompt_usuario = input("Apresente o nome de um produto: ")

    resposta = cliente.chat.completions.create(
            messages=[
                    {
                            "role" : "system",
                            "content" :prompt_sistema
                    },
                    {
                            "role" : "user",
                            "content" :nome_produto
                    }
            ],
            model=modelo,
            #criatividade 0 sem 2 Maximo mas pode trazer elementos que não são do mundo real
            temperature=0,
            max_tokens=200,
            #numero de respostas
            n=0
    )
    return resposta.choices[0].message.content
#print(resposta.choices[0].message.content)
#for contador in range(0,3):
#    print(resposta.choices[contador].message.content)


####### Inicio da interação com o Usuário em tela ########
categorias_validas = input("Informe as categorias válidas, separando por vígula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)