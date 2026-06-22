from sqlalchemy import text
from app.db.database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_database();"))

        for row in result:
            print(f"Connected to: {row[0]}")

except Exception as e:
    print("Connection failed:")
    print(e)