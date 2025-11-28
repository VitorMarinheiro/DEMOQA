# language: pt
Funcionalidade: Interação com Janelas do Navegador
  Como um usuário
  Eu quero interagir com múltiplas janelas do navegador
  Para garantir que a aplicação lida corretamente com novos contextos de janela

  @browser_windows
  Cenário: Abrir e validar uma nova janela
    Dado que eu esteja na página de Browser Windows
    Quando eu abrir uma nova janela
    Então o conteúdo da nova janela deve ser validado com sucesso