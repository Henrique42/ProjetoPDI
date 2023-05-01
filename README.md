# ProjetoPDI: Reconhecimento de Figuras

## 1. Introdução
O objetivo deste projeto é ler um arquivo de imagem binária *.pbm*, que pode conter *n* objetos pretos, com ou sem buracos, em um fundo branco e retornar a quantidade total de objetos na imagens e quantos deles possuem buracos.

- Exemplo de imagem alvo:

<img src="https://user-images.githubusercontent.com/39635299/235477112-de2810ec-ce0e-49b0-addd-a1a66ecafb06.png" alt="Imagem de exemplo"  width="240" height="320">

### 1.1. Observações
- Este trabalho é referente ao projeto final da disciplina de *Processamento de Imagens*.
- Desenvolvido em *Python*, sem o uso de bibliotecas externas.
- O algoritmo reconhece objetos e buracos de quaisquer formatos.


## 2. Organização do projeto
- Divisão das pastas:

```
.
├── Contagem
│   ├── imagem.py     
│   └── operacoes.py  
├── main.py
├── README.md
├── Resultados        
│   └── nova.pbm      
└── Testes
    ├── 01.pbm        
    ├── 02.pbm        
    ├── 03.pbm        
    └── 04.pbm        

3 directories, 9 files
```

- [/main.py](/main.py): arquivo que inicia o projeto. É ele que deve ser executado.
- [/Contagem/imagem.py](/Contagem/imagem.py): arquivo no qual está a classe que define os objetos de imagem a serem manipulados pelo sistema.
- [/Contagem/operacoes.py](/Contagem/operacoes.py): arquivo no qual estão os métodos que realizam a contagem de figuras e buracos.
- [/Testes](/Testes): pasta na qual estão as imagens de teste do projeto.
- [/Resultados](/Resultados): pasta na qual são colocadas as imagens salvas no projeto (ver 3.1. Opcional).


## 3. Execução
- Basta executar o arquivo *main.py*, contido na raiz do projeto.

```
python main.py
```

- Durante a execução, o sistema irá pedir o nome do arquivo alvo. Estes arquivos *.pbm*, por padrão, são colocados na pasta *"/Testes"* e, para executá-los, basta digitar o nome do arquivo sem a sua extensão (ex.: 04). Também é possível adicionar novos arquivos de teste na pasta.

- Exemplo de tela durante a execução:

![tela_inicio](https://user-images.githubusercontent.com/39635299/235484009-3f15e8f2-8a44-48f0-9c1c-6d48ea926fba.png)

### 3.1. Opcional
- Também é possível salvar um arquivo ao retirar o comentário da seguinte linha de código no arquivo *main.py*:

```
#salvarImagem(imagem)
```

- O processo de salvar é similar ao de ler um arquivo. Os arquivos são salvos na pasta *"/Resultados"*.


## 4. Resultados
- O sistema finaliza a sua execução ao imprimir a quantidade de objetos encontrados e quantos buracos existem em cada um deles.

- Exemplo de tela após a execução:

![tela_resultados](https://user-images.githubusercontent.com/39635299/235483507-b3ebff21-ac12-4c63-bb4f-e835bb578a46.png)


## 5. Equipe:
- Bruno Henrique de Jesus Silva
- Gustavo de Farias Souza Almeida
- João Pedro da Silva Santos
- Matheus Lima Pinheiro
