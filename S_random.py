import secrets

secure_generator = secrets.SystemRandom()


print("This is from secret module =>",secure_generator.random())

#for integer number

print("From randint =>",secure_generator.randint(10,100))

print("From randrange => ",secure_generator.randrange(0,200,5))

#for float number

print("From uniform method => ",secure_generator.uniform(0,10))

print("From triangular method => ",secure_generator.triangular(0,10,3))

secure_generator.seed(3)

print("From Seed() => ",secure_generator.random())

list1 = [1,2,3,4,5,6,7,812,34,56,78,90]

print("From sample() =>",secure_generator.sample(list1,3))

choice = secure_generator.choice(list1)

print("From choice() => ",choice)

secure_generator.shuffle(list1)

print("From shuffle() => ",list1)

#Token

print("From Tokenbyte() => ",secrets.token_bytes(2))

print("From token_hex => ",secrets.token_hex(4))


reset_link = "phonne//123-https//reset="

code = secrets.token_urlsafe()


comp_link = reset_link+code

print("From urlsafe  code => ",comp_link)