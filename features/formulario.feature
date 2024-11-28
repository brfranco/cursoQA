Feature: Preencher formulário de contato

  Scenario: Enviar formulário de contato
    Given estou na página de contato
    When preencho o formulário com "Seu Nome" e "seuemail@exemplo.com"
    And escolho "Ser facilitador" no menu
    And escrevo a mensagem "Teste - Oi!"
    Then envio o formulário

