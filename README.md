# Gestão de Finanças Pessoais
Esse projeto tem objetivo de gerar uma base de dados para analise de gastos e projeção de gastos por uma pessoa

### Banco de Dados
O banco de dados escolhido para armazenar as informações foi o Access. Essa escolha foi feita pela facilidade de ter esse SGBD, visto que faz parte do pacote office. Além do Acces o DBeaver foi usado para consulta e analise da base de dados.

### Histórico do Cartão de Crédito
Esse script faz e leitura de arquivos baixados no Home Bancking e faz a carga na base do Access.
Ele além de fazer leitura e carga ele faz atualização automática da base, caso um arquivo já carregado venha a ser disponibilizado para leitura.
Esse script também faz ajustes na classificação dos lançamentos.

```
CREATE TABLE historico_cartao (
  [Codigo] INTEGER,
  [Cartao] CHAR(20),
  [Data_Compra] DATE,
  [Lancamento] CHAR(50),
  [Tipo_Lancamento] CHAR(20),
  [Valor] DECIMAL(10,4),
  [Parcela] CHAR(6),
  [Lancada] BOOLEAN,
  [Vencimento] DATE,
  [Arquivo] CHAR(50)
);
```

### Histório Conta Corrente
Esse script faz e leitura de arquivos baixados no Home Bancking e faz a carga na base do Access.
Ele além de fazer leitura e carga ele faz atualização automática da base, caso um arquivo já carregado venha a ser disponibilizado para leitura.
Esse script também faz ajustes na classificação dos lançamentos.

```
CREATE TABLE extrato_cc (
	[Codigo] INTEGER,
	[Data_Lancamento] DATE,
	[Dependencia_Origem] CHAR(50),
	[Historico] CHAR(50),
	[Tipo_Historico] CHAR(20),
	[Data_Balancete] DATE,
	[numero_documento] CHAR(20),
	[Valor] DECIMAL(10,4),
	[mes_extrato] CHAR(6),
);
```

### Previsão de Lançamento
Esse script faz a leitura da base de cartão e conta corrente e faz previsão de lançamento de acordo com premissa imppostas no script, as quais são:
* Compras Parceladas da Ultima Fatura: Nesse método o script verifica os valores lançados na ultima fatura e que ainda não estão presentes na fatura em aberta do cartão de crédito
* Compras Processadas: Esse método apenas repassa os lançamentos para próxima fatura já lançadas na fatura aberta
* Compras Recorrentes: Esse método faz o lançamentos de compras que todo mês são cobradas no cartão de crédito e que não foi lançado ainda na fatura. Esses valores não são compras parcelas, apenas serviços ou valores que são lançados todo mês no cartão
* Lançamentos Recorrentes em conta correte: Esse método faz o lançamentos de compras que todo mês são cobradas em conta corrente.

```
CREATE TABLE previsao_lancamento (
	[Data_Lancamento] DATE,
	[Historico] CHAR(50),
	[Tipo_Historico] CHAR(20),
	[valor] DECIMAL(10,4),
	[Data_Base] CHAR(10),
	[Local_Lancado] CHAR(50),
	[Metodo] CHAR(50)
);
```

### Regra de Convesão
Essa tabela foi criada para conter regras de conversão. Nela temos o tipo da regra a ser consultada e a condição chave x valor.

```
CREATE TABLE regra_conversao (
  [nome_regra] CHAR(50),
  [chave] CHAR(50),
  [valor] CHAR(50)
);
```

### gestao.py
Esse .py contém uma classe para fazer todo o trabalho por traz para acesso ao Access. Na instanciação da classe ele faz a conexão com a base de dados.

### Power BI
Um power BI foi gerado para fazer a leitura da base e disponiblizar de forma visual os dados disponiveis nas diferentes bases. Por questão de segurança esse power bi não está disponivel nesse repositorio.
