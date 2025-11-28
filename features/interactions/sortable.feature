# language: pt
Funcionalidade: Ordenação de Itens
  Como um usuário
  Eu quero ordenar os itens de uma lista
  Para organizá-los da maneira que eu preferir

  @sortable
  Cenário: Ordenar itens em ordem decrescente
    Dado que eu esteja na página de Ordenação
    Quando eu ordenar os itens em ordem decrescente
    Então os itens devem estar em ordem decrescente