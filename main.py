
# backend/app/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal
from passlib.context import CryptContext
import jwt
from .models import User  # Assuming the User model is defined in models.py
import boto3
import os
from dotenv import load_dotenv
from fastapi import File, UploadFile

app = FastAPI()

# Password hashing and verification setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "yoursecretkey"  # Replace with a strong, secure key

# Dependency to get database session
def get_db():    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

# Simple root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Document Management API!"}

# Signup endpoint
@app.post("/signup")
async def signup(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, email=email, password_hash=get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)  # Ensures the user object is refreshed with the new ID
    return {"message": "User created successfully"}

# Login endpoint
@app.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password_hash):
        token = create_access_token(data={"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

@app.post("/upload")
async def upload_and_parse_document(file: UploadFile = File(...)):
    # Upload to S3
    s3_client.upload_fileobj(
        file.file,
        os.getenv("AWS_S3_BUCKET_NAME"),
        file.filename
    )

    # Parse document content
    file.file.seek(0)  # Reset file pointer after upload
    content = parse_document(file.file)
    return {
        "message": f"File '{file.filename}' uploaded and parsed successfully",
        "content": content
    }
 
load_dotenv()  # Load credentials from .env

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AKIAQ3EGT6MMFDNXHRDB"),
    aws_secret_access_key=os.getenv("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")
)