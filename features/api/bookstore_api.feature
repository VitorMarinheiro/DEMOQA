# language: pt
Funcionalidade: API da Livraria
  Como um usuário da API
  Eu quero gerenciar minha coleção de livros
  Para que eu possa manter minha lista de leitura atualizada

  @bookstore_api
  Cenário: Adicionar livros à coleção de um usuário
    Dado um usuário é criado com sucesso
    Quando eu adiciono dois livros à sua coleção
    Então os livros devem ser listados nos detalhes do usuário