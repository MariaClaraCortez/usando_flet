import sqlite3

def conectar_bd():
    conexao = sqlite3.connect("bd_tarefa.sqlite")
    cursor = conexao.cursor
    return conexao, cursor