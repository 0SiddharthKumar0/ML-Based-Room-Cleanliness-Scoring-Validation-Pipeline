from app.auth.security import (
    hash_password,
    verify_password
)

password = "admin123"

hashed = hash_password(password)

print("Hash:", hashed)

print(
    "Valid:",
    verify_password(
        "admin123",
        hashed
    )
)