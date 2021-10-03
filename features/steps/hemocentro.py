# pylint: disable=function-redefined
# pylint: disable=no-name-in-module
from behave import given, when, then
from selenium.webdriver.common.by import *
from time import sleep
import pandas as pd

@given(u'que eu estou na url "http://www.hemocentro.unicamp.br/"')
def step_impl(context):
    context.driver.get("http://www.hemocentro.unicamp.br/")

@when(u'eu acesso a url')
def step_impl(context):
    assert True is not False

@then(u'eu pego as informações de tipo sanguíneo e data de atualização')
def step_impl(context):
    ultimaAtualizacao = context.driver.find_element_by_xpath("//p[@class='ultima-atualizao']").text
    sangueOPositivo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'O+')]/..").text
    sangueAPositivo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'A+')]/..").text
    sangueABPositivo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'AB+')]/..").text
    sangueONegativo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'O-')]/..").text
    sangueANegativo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'A-')]/..").text
    sangueABNegativo = context.driver.find_element_by_xpath("//div[@class='bolsa' and contains(.,'AB-')]/..").text
    tipoSanguineo = [sangueABPositivo,sangueANegativo,sangueOPositivo,sangueAPositivo,sangueONegativo,sangueABNegativo]
    hemocentro = pd.DataFrame({'Atualizacao':ultimaAtualizacao,'Tipos Saguineos':tipoSanguineo})
    print(hemocentro)
