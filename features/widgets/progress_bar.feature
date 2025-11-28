# language: pt
Funcionalidade: Barra de Progresso
  Como um usuário
  Eu quero interagir com a barra de progresso
  Para garantir que ela funcione conforme o esperado

  @progress_bar
  Cenário: Validar o preenchimento completo da barra de progresso
    Dado que eu esteja na página da Barra de Progresso
    Quando eu iniciar a barra de progresso
    Então a barra de progresso deve atingir 100%