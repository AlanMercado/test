# -*- coding: utf-8 -*-
from lettuce import step, world
from Calculadora import Calculadora
from edad import edad

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" menos "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" por "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_por_group1(step,num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" entre "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_entre_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.divicion(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" ala "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_ala_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))

@step(u'Dado que ingreso el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(int(num1))

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, num1):
    world.cal = Calculadora()
    world.cal.edad(int(num1))

@step(u'Dado que ingreso el id de la figura "([^"]*)" y los datos necesarios "([^"]*)" "([^"]*)" "([^"]*)"')
def dado_que_ingreso_el_id_de_la_figura_group1_y_los_datos_necesarios_group2_group3_group3(step, num1, num2, num3, num4):
    world.cal = Calculadora()
    world.cal.area(int(num1),int(num2),int(num3),int(num4))


@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    assert str(esperado) == str(world.cal.obtener_resultado()),'El resultado esperado es ' +str(esperado)+ ' y el obtenido es ' +str(world.cal.obtener_resultado())
