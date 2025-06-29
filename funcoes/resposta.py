from bs4 import BeautifulSoup
import re

with open("page/revio-e-commerce.html", "r", encoding="utf-8") as file:
    pagina = BeautifulSoup(file, "html.parser")


def converter_preco(preco_str: str):
    return float(preco_str.replace("R$", "").replace(".", "").replace(",", "."))

# Função para o 1º endpoint, pesquisa por nome de geladeira
def informacoes_geladeira(nome:str):
    if pagina.find(string=re.compile(f"{nome}")) and nome:
        informacoes = {}
        informacoes['nome'] = pagina.find(string=re.compile(f"{nome}"))
        div_geladeira = informacoes['nome'].parent.parent

        if div_geladeira.find("span", attrs={"class":"current-price"}):
            preco = div_geladeira.find("span", attrs={"class": "current-price"}).text.strip()
            informacoes['valor'] = converter_preco(preco)
            informacoes['nota'] = float(div_geladeira.find("span", attrs={"class":"rating-value"}).text.strip())

            return informacoes
    return None

# Função para o 2º endpoint, retorna todas as geladeiras dentro do intervalo de preço
def intervalo_preco(min_preco: float, max_preco: float):
    lista_produtos = []
    for produto in pagina.find_all("div", attrs={"class": "product-card"}):
        dados_produto = {}
        preco_texto = produto.find("span", attrs={"class": "current-price"}).text.strip()
        preco = converter_preco(preco_texto)
        if preco >= min_preco and preco <= max_preco:
            dados_produto['nome'] = produto.find("h3").text.strip()
            dados_produto['valor'] = preco
            dados_produto['nota'] = float(produto.find("span", attrs={"class": "rating-value"}).text.strip())
            lista_produtos.append(dados_produto)
    return lista_produtos


# Função para o 2º endpoint, retorna todas as geladeiras dentro do intervalo de notas
def intervalo_nota(min_nota: float, max_nota: float):
    lista_produtos = []
    for produto in pagina.find_all("div", attrs={"class": "product-card"}):
        dados_produto = {}
        nota = float(produto.find("span", attrs={"class":"rating-value"}).text.strip())
        if nota >= min_nota and nota <= max_nota:
            dados_produto['nome'] = produto.find("h3").text.strip()
            dados_produto['valor'] = converter_preco(produto.find("span", attrs={"class": "current-price"}).text.strip())
            dados_produto['nota'] = float(produto.find("span", attrs={"class": "rating-value"}).text.strip())
            lista_produtos.append(dados_produto)
    return lista_produtos
            

if __name__ == "__main__":
    print(intervalo_preco(1000, 3000))