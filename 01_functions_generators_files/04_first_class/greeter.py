def greet(language):
    match language:
        case 'en':
            print('Hello!')
        case 'es':
            print('Hola!')
        case 'fr':
            print('Bonjour!')

greet('fr')         # Bonjour!
greet('es')         # Hola!


def create_greeter(language):
    match language:
        case "en":
            return lambda: print("Hello")
        case "es":
            return lambda: print("Hola!")
        case "fr":
            return lambda: print("Bonjour!")
        case _:
            return lambda: print("I don't know that language")


es_greeter = create_greeter("es")
es_greeter()  # type: ignore # Hola!
es_greeter()  # Hola!
es_greeter()  # Hola!

en_greeter = create_greeter("en")
en_greeter()  # Hello
