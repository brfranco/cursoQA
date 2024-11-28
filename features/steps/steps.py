from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@given('estou na página de contato')
def step_estou_na_pagina_de_contato(context):
    # Inicializa o driver do navegador (Chrome)
    context.driver = webdriver.Chrome()  # Substitua pelo driver adequado se necessário
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")
    time.sleep(2)  # Aguarde para garantir que a página foi carregada

@when('preencho o formulário com "{nome}" e "{email}"')
def step_preencho_formulario(context, nome, email):
    # Preenche os campos de Nome e Email
    context.driver.find_element(By.NOME, "name").send_keys(nome)
    context.driver.find_element(By.NOME, "email").send_keys(email)

@when('escolho "{opcao}" no menu')
def step_escolho_opcao_menu(context, opcao):
    # Seleciona a opção no menu drop-down
    dropdown = Select(context.driver.find_element(By.NAME, "assunto"))
    dropdown.select_by_visible_text(opcao)

@when('escrevo a mensagem "{mensagem}"')
def step_escrevo_mensagem(context, mensagem):
    # Preenche o campo de mensagem
    context.driver.find_element(By.NAME, "message").send_keys(mensagem)

@then('envio o formulário')
def step_envio_formulario(context):
    # Clica no botão de enviar
    context.driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
    time.sleep(2)  # Aguarda o envio
    context.driver.quit()  # Fecha o navegador
