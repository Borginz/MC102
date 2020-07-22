 import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help = "argumento para executar aplicativo")
    parser.add_argument("operacoes",help = "operacoes em agenda")
    args = parser.parse_args()

