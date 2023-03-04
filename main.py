from os import getenv
from dotenv import load_dotenv


# load environment variables from .env file
load_dotenv()
print(getenv("FIRST_NAME"))
# establish connection
