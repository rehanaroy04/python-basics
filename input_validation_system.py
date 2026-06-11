class ValidationError(Exception):
    pass

class AgeTooYoungError(ValidationError):
    pass

class AgeTooOldError(ValidationError):
    pass

class InvalidEmailError(ValidationError):
    pass

class InvalidPhoneError(ValidationError):
    pass

def validate_age(age):
    if not isinstance(age, (int, float)):
        raise ValidationError("Age must be a number")
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age < 18:
        raise AgeTooYoungError(f"Age {age} is too young. Minimum age is 18")
    if age > 120:
        raise AgeTooOldError(f"Age {age} is too old. Maximum age is 120")
    return True

def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError("Email must contain @ symbol")
    if '.' not in email.split('@')[1]:
        raise InvalidEmailError("Email must contain domain extension")
    return True

def validate_phone(phone):
    if not phone.isdigit():
        raise InvalidPhoneError("Phone number must contain only digits")
    if len(phone) not in [10, 11]:
        raise InvalidPhoneError("Phone number must be 10 or 11 digits")
    return True

def validate_name(name):
    if len(name.strip()) < 2:
        raise ValidationError("Name must be at least 2 characters")
    if not name.replace(" ", "").isalpha():
        raise ValidationError("Name must contain only letters and spaces")
    return True

print("=" * 40)
print("USER INPUT VALIDATION SYSTEM")
print("=" * 40)

while True:
    try:
        name = input("Enter name: ")
        validate_name(name)
        break
    except ValidationError as e:
        print(f"Error: {e}\n")

while True:
    try:
        age = int(input("Enter age: "))
        validate_age(age)
        break
    except AgeTooYoungError as e:
        print(f"Error: {e}")
    except AgeTooOldError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ValidationError as e:
        print(f"Error: {e}")

while True:
    try:
        email = input("Enter email: ")
        validate_email(email)
        break
    except InvalidEmailError as e:
        print(f"Error: {e}")

while True:
    try:
        phone = input("Enter phone number: ")
        validate_phone(phone)
        break
    except InvalidPhoneError as e:
        print(f"Error: {e}")

print("\n" + "=" * 40)
print("VALIDATION SUCCESSFUL!")
print("=" * 40)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print("=" * 40)