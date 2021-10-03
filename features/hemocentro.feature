#language: pt

Funcionalidade: Acessar a URL do Hemocentro e buscar o tipo sanguíneo e a data de atualização

Cenário: Acessando a URL com sucesso e buscando as informações
    Dado que eu estou na url "http://www.hemocentro.unicamp.br/"
    Quando eu acesso a url
    Então eu pego as informações de tipo sanguíneo e data de atualização

