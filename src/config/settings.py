from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    """ AWS_REGION = os.getenv("AWS_REGION")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME") """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")
    ENVIRONMENT = os.getenv("ENVIRONMENT")    
    

settings = Settings()