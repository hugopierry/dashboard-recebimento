# Tratamento de Dados para Power BI

Este projeto consiste em um script desenvolvido em Python para realizar o tratamento e a organização de dados provenientes de arquivos **CSV ou Excel**, preparando as informações para uma análise mais confiável no Power BI.

O objetivo é automatizar tarefas de limpeza que, quando não realizadas, podem prejudicar a análise final dos dados.

## O que o script faz

Ao executar o arquivo responsável pelo tratamento, o script realiza automaticamente etapas como:

* Remoção de dados nulos;
* Identificação e tratamento de células em branco;
* Remoção de espaços desnecessários;
* Organização dos dados;
* Padronização das informações;
* Geração de um novo arquivo com os dados tratados.

A ideia é evitar que informações desnecessárias ou inconsistentes sejam levadas para a etapa de análise.

## Integração com Power BI

Após o tratamento, o arquivo gerado pode ser utilizado como fonte de dados no **Power BI**.

O fluxo do projeto funciona da seguinte forma:

**Arquivo CSV/Excel → Python → Tratamento dos dados → Arquivo tratado → Power BI**

Depois que a fonte de dados estiver configurada no Power BI, basta executar novamente o processo de tratamento quando houver uma nova atualização dos dados e, em seguida, atualizar o Power BI.

Dessa forma, os dados já estarão preparados para serem utilizados nos relatórios e dashboards.

## Objetivo do projeto

O projeto foi desenvolvido com foco em **automação, tratamento de dados e integração com ferramentas de análise**, buscando tornar o processo mais simples, organizado e confiável.

A proposta é transformar uma etapa que poderia ser realizada manualmente em um processo automatizado:

**Executar o script → dados tratados → atualizar o Power BI → análise pronta.**

## Tecnologias utilizadas

* Python
* Pandas
* CSV / Excel
* Power BI

## Próximos passos

O projeto poderá receber novas etapas de tratamento e validação, tornando o processo cada vez mais automatizado e preparado para diferentes tipos de bases de dados.
