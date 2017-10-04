Feature: Multiplicacion de dos numeros
    Como usuario de la calculadora
    deseo realizar la multiplicacion de dos numeros
    para obtener el resultado preciso

    Scenario: Multiplicacion de 2 por dos
        Dado que ingreso los numeros "2" por "2"
        cuando realizo la operación
        entonces obtengo el resultado "4"

    Scenario: multiplicacion de 7 por cinco
        Dado que ingreso los numeros "7" por "5"
        cuando realizo la operación
        entonces obtengo el resultado "35"

    Scenario: multiplicacion de 5 por 5
        Dado que ingreso los numeros "5" por "5"
        cuando realizo la operación
        entonces obtengo el resultado "25"

    Scenario: Multiplicacion de 1000 por 100
        Dado que ingreso los numeros "1000" por "100"
        cuando realizo la operación
        entonces obtengo el resultado "100000"