# ProjetoPDI

## Introdução
O objetivo deste projeto é ler um arquivo de imagem binário *.pbm*, que pode conter *n* objetos pretos, com ou sem buracos, em um fundo branco e retornar a quantidade total de objetos na imagens e quantos deles possuem buracos.

### Observações
- Este trabalho é referente ao projeto final da disciplina de *Processamento de Imagens*.
- Desenvolvido em *Python*, sem o uso de bibliotecas externas.
 
## Execução
- Basta executar o arquivo *main.py*, contido na raiz do projeto.

- Durante a execução, o sistema irá pedir o nome do arquivo alvo. Estes arquivos *.pbm*, por padrão, são colocados na pasta *"/Testes"* e, para executá-los, basta digitar o nome do arquivo sem a sua extensão (ex.: 03). Também é possível adicionar novos arquivos de teste na pasta.

- Também é possível salvar um arquivo ao retirar o comentário da seguinte linha de código no arquivo *main.py*:

```
#salvarImagem(imagem)
```

- O processo de salvar é similar ao de ler um arquivo. Os arquivos são salvos na pasta *"/Resultados"*.

## Resultados
- O sistema finaliza a sua execução ao imprimir a quantidade de objetos encontrados e quantos buracos existem em cada um deles.

## Equipe:
- Bruno Henrique de Jesus Silva
- Gustavo de Farias Souza Almeida
- João Pedro da Silva Santos
- Matheus Lima Pinheiro
