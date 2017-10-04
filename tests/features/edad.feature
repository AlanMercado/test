Feature: tipo de usuario segun su edad
    Como usuario del sistema de edad
    deseo realizar la prueba de que tipo de usuario soy
    para obtener el resultado preciso

    Scenario: edad de -1
        Dado que ingreso la edad "-1"
        cuando realizo la operación
        entonces obtengo el resultado "no existes"

    Scenario: edad de 2
        Dado que ingreso la edad "2"
        cuando realizo la operación
        entonces obtengo el resultado "eres nino"

    Scenario: edad de 17
        Dado que ingreso la edad "17"
        cuando realizo la operación
        entonces obtengo el resultado "eres adolecente"

    Scenario: edad de 25
        Dado que ingreso la edad "25"
        cuando realizo la operación
        entonces obtengo el resultado "eres adulto"

    Scenario: edad de 68
        Dado que ingreso la edad "68"
        cuando realizo la operación
        entonces obtengo el resultado "eres adulto mayor"

    Scenario: edad de 150
        Dado que ingreso la edad "150"
        cuando realizo la operación
        entonces obtengo el resultado "eres mumm-ra"