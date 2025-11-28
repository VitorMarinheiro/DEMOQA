# language: pt
Funcionalidade: Formulário de Prática
  Como um usuário
  Eu quero preencher e submeter o formulário de prática
  Para garantir que meus dados sejam registrados corretamente

  @practice_form
  Cenário: Preenchimento e submissão bem-sucedidos do formulário
    Dado que eu esteja na página inicial
    Quando eu navegar para a página de formulário de prática
    E eu preencher o formulário com dados válidos
    Então eu devo ver um popup de confirmação com os dados submetidos