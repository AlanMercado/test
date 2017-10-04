Feature: area de figuras geometricas
    Como usuario del sistema de area
    deseo escojer el tipo de figura para obtener su area
    para obtener el resultado preciso

    Scenario: area de un cuadrado
        Dado que ingreso el id de la figura "1" y los datos necesarios "5" "0" "0"
        cuando realizo la operación
        entonces obtengo el resultado "25"

    Scenario: area de un rectangulo
        Dado que ingreso el id de la figura "2" y los datos necesarios "5" "2" "0"
        cuando realizo la operación
        entonces obtengo el resultado "10"

    Scenario: area de un circulo
        Dado que ingreso el id de la figura "3" y los datos necesarios "5" "0" "0"
        cuando realizo la operación
        entonces obtengo el resultado "78.54"

    Scenario: area de un trapecio
        Dado que ingreso el id de la figura "4" y los datos necesarios "2" "2" "2"
        cuando realizo la operación
        entonces obtengo el resultado "4"
