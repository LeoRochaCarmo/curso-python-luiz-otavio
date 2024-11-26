# Exercício - Salve sua classe em JSON
import json

caminho_arquivo = '.\\03_programacao_orientada_a_objetos\\dados\\instancia_salva_em_json.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Leonardo', 31)
p2 = Pessoa('Leandro', 32)
p3 = Pessoa('Lenice', 33)
bd = [vars(p1),vars(p2),vars(p3)]

def fazer_dump():
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ESSE É O MAIN')
    fazer_dump()