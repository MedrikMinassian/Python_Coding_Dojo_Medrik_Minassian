

person={
    "first": "Ada",
    "last": "Lovelace",
    "age": 42,
    "is_organ_donor": True
}
# person ["email"] = "alovelace@codingdojo.com"

if "email" not in person:
    person["email"] = "wrongemail@email.com"

print(person["email"])    