from faker import Faker

fake = Faker()

# Генерация фейковых валидных данных
user_data = {
    'nickname': fake.user_name(),
    'email': fake.email(),
    'password': fake.password()
}

auth_user_data = {
    'username': 'john',
    'password': 'poker'
}
