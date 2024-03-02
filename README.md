#### Esse projeto faz parte da edição do bootcamp Dio.io
# **Potência Tech powered by iFood | Ciência de Dados**

**Instrutor: </br> Guilherme Arthur de Carvalho**
*Analista de sistemas*
*@decarvalhogui*

## Desafio
### Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja  odernizar suas operações e para isso escolheu a linguagem Python#. Para a primeira versão do sistema devemos implementar apenas 3 operações: 
1. ### Depósito, Operação de depósito
        Deve ser possível depositar valores positivos para a minha
        conta bancária. A vl do projeto trabalha apenas com 1
        usuário, dessa forma não precisamos nos preocupar em
        identificar qual é o número da agência e conta bancária. Todos
        os depósitos devem ser armazenados em uma variável e
        exibidos na operação de extrato.
2. ### Saque, Operação de saque
        O sistema deve permitir realizar 3 saques diários com limite
        máximo de R$ 500,00 por saque. Caso o usuário não tenha
        saldo em conta, o sistema deve exibir uma mensagem
        informando que não será possível sacar o dinheiro por falta de
        saldo. Todos os saques devem ser armazenados em uma
        variável e exibidos na operação de extrato.
3. ### Extrato, Operação de extrato
        Essa operação deve listar todos os depósitos e saques
        realizados na conta. No fim da listagem deve ser exibido o
        saldo atual da conta. Se o extrato estiver em branco, exibir a
        mensagem: Não foram realizadas movimentações.
        Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
        exemplo: 1500.45 = R$ 1500.45


## Como Executar o Código Python

### Instalação do Python:
1. Primeiro, você precisa ter o Python instalado em seu computador. Se ainda não o tem, siga os passos abaixo:
   - Acesse o [site oficial do Python](https://www.python.org/).
   - Baixe o instalador apropriado para o seu sistema operacional (Windows, macOS ou Linux).
   - Execute o instalador e siga as instruções para concluir a instalação.

### Ambiente Virtual (Opcional):
- É recomendável configurar um ambiente virtual para isolar as dependências do seu projeto. Isso evita conflitos entre pacotes e garante a organização.
- Você pode usar ferramentas como `virtualenv` ou `Anaconda` para criar um ambiente virtual. Escolha a que preferir.
- Para criar um ambiente virtual com `virtualenv`, execute o seguinte comando no terminal:

        pip install virtualenv
        virtualenv meu_ambiente
        source meu_ambiente/bin/activate # No Windows: meu_ambiente\Scripts\activate



### Escrevendo e Executando o Código:
1. Crie um arquivo chamado `main.py` (ou outro nome de sua escolha) e escreva o código da classe `ContaBancaria` e o menu interativo.
2. Salve o arquivo.
3. Abra o terminal e navegue até o diretório onde o arquivo `main.py` está localizado.
4. Execute o programa Python digitando o seguinte comando:

        python main.py
        O Python interpretará e executará o código contido no arquivo especificado.
5. Siga as instruções do menu para realizar depósitos, saques, extratos ou sair do programa.

### Interpretação dos Resultados:
- Após executar o programa, verifique a saída exibida no terminal.

## Lembre-se de adaptar o código conforme suas necessidades específicas e aproveite o seu sistema bancário em Python! 😉