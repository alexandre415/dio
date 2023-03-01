import phonenumbers

from phonenumbers import geocoder

telefone = input('Digite o seu telefone: ')

phone_number = phonenumbers.parse(telefone)

print(geocoder.description_for_number(phone_number, 'pt'))