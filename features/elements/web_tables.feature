# language: pt
Funcionalidade: Gerenciamento de Registros em Web Tables
  Como um usuário
  Eu quero adicionar, editar e excluir registros em uma tabela
  Para garantir que os dados possam ser gerenciados corretamente

  @web_tables
  Cenário: Ciclo de vida completo de um registro na tabela
    Dado que eu esteja na página de Web Tables
    Quando eu adicionar um novo registro
    E eu editar o registro recém-adicionado
    Então o registro deve ser atualizado com sucesso
    Quando eu excluir o registro
    Então o registro não deve mais existir na tabela