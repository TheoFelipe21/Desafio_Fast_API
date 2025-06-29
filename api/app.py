from fastapi import FastAPI
import sys
sys.path.append("..")
from funcoes.resposta import *

app = FastAPI()

@app.get("/informacoes_geladeira")
def informacoes_por_nome(nome:str):

    """Busca as informações da geladeira por nome"""
    
    geladeira = informacoes_geladeira(nome)
    if geladeira:
        return geladeira
    return {"error": "Geladeira não encontrada"}


@app.get("/intervalo_preco")
def geladeiras_por_preco(min_preco: float, max_preco: float):

    """Busca as geladeiras dentro do intervalo de preços"""
    
    geladeiras = intervalo_preco(min_preco, max_preco)
    if geladeiras:
        return geladeiras
    return {"error": "Geladeiras não encontrada"}


@app.get("/intervalo_nota")
def geladeiras_por_nota(min_nota: float, max_nota: float):

    """Busca as geladeiras dentro do intervalo de notas"""
    
    geladeiras = intervalo_nota(min_nota, max_nota)
    if geladeiras:
        return geladeiras
    return {"error": "Geladeiras não encontrada"}

