from bs4 import BeautifulSoup
import re

with open("page/revio-e-commerce.html", "r", encoding="utf-8") as file:
    pagina = BeautifulSoup(file, "html.parser")

# Função para o 1º endpoint, pesquisa por nome de geladeira
def informacoes_geladeira(nome:str):
    if pagina.find(string=re.compile(f"{nome}")) and nome:
        informacoes = {}
        informacoes['nome'] = pagina.find(string=re.compile(f"{nome}"))
        div_geladeira = informacoes['nome'].parent.parent

        if div_geladeira.find("span", attrs={"class":"current-price"}):
            informacoes['preco'] = div_geladeira.find("span", attrs={"class":"current-price"}).text.strip()
            informacoes['rating'] = div_geladeira.find("span", attrs={"class":"rating-value"}).text.strip()
            informacoes['parcelas'] = div_geladeira.find("div", attrs={"class":"installments"}).text.strip()

            return informacoes
    return None

# Função para o 2º endpoint, retorna todas as geladeiras dentro do intervalo de preço
def intervalo_preco(min_preco: float, max_preco: float):
    produtos_no_intervalo = {}
    for produto in pagina.find_all("div", attrs={"class": "product-card"}):
        preco_texto = produto.find("span", attrs={"class": "current-price"}).text.strip()
        preco = float(preco_texto.replace("R$", "").replace(".", "").replace(",", "."))
        if preco >= min_preco and preco <= max_preco:
            nome_produto = produto.find("h3").text.strip()
            produtos_no_intervalo[nome_produto] = preco
    return produtos_no_intervalo
            
# Função para o 2º endpoint, retorna todas as geladeiras dentro do intervalo de notas
def intervalo_nota(min_nota: float, max_nota: float):
    produtos_no_intervalo = {}
    for produto in pagina.find_all("div", attrs={"class": "product-card"}):
        nota = float(produto.find("span", attrs={"class":"rating-value"}).text.strip())
        if nota >= min_nota and nota <= max_nota:
            nome_produto = produto.find("h3").text.strip()
            produtos_no_intervalo[nome_produto] = nota
    return produtos_no_intervalo
            

if __name__ == "__main__":
    pass