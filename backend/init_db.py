from database import Base, engine  # Import your database setup
import models  # Import your models so that they're registered with SQLAlchemy

# This will create the tables in the database based on your models
Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")
