Feature: divicion de dos numeros
    Como usuario de la calculadora
    deseo realizar la divicion de dos numeros
    para obtener el resultado preciso

    Scenario: divicion de 2 entre dos
        Dado que ingreso los numeros "2" entre "2"
        cuando realizo la operación
        entonces obtengo el resultado "1"

    Scenario: divicion de 10 entre cinco
        Dado que ingreso los numeros "10" entre "5"
        cuando realizo la operación
        entonces obtengo el resultado "2"

    Scenario: divicion de 25 entre 5
        Dado que ingreso los numeros "25" entre "5"
        cuando realizo la operación
        entonces obtengo el resultado "5"

    Scenario: divicion de 1000 entre 100
        Dado que ingreso los numeros "1000" entre "100"
        cuando realizo la operación
        entonces obtengo el resultado "10"