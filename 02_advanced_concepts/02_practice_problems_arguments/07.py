def register(username, /, age, *, password):
    return {'username': username, 'password': password, 'age': age}

print(register("Raymond", 38, password="filibuster"))
print(register("Regina", password="sport", age=63))
print(register(age=35, "Michael", password="Elsa")) # Raises Error
