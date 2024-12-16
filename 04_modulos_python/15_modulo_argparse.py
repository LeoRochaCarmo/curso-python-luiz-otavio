# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Preciso de ajuda"',
    # type=list,
    metavar='STRING',
    # default='Olá mundo', # Valor padrão 
    required=False,
    # nargs='+', Recebe mais de uma valor
    action='append' # Recebe o argumento mais de uma vez
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)