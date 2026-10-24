from src.services.processamento import criar_pessoa, criar_arquivo
from src.models.pessoa_arquivo import ArquivoPessoaErro

def main():
    pessoa = criar_pessoa()
    print(pessoa.apresentar())

    try:
        arquivo_pessoa = criar_arquivo()
        print(arquivo_pessoa.apresentar())
        print("Arquivo Salvo em: ", arquivo_pessoa.salvar())
    except ArquivoPessoaErro as erro:
        print(f"Erro: {erro}")

if __name__ == "__main__":
    main()