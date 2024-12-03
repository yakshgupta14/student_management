from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection string
MONGO_URI = "mongodb+srv://studentuser:<db_password>@studentmanagement.xbsbe.mongodb.net/"

# Replace <db_password> with the actual password
MONGO_URI = MONGO_URI.replace("<db_password>", "studentuser")

# Create MongoDB client and connect to the database
client = AsyncIOMotorClient(MONGO_URI)

# Select the database and collection
database = client["student_management"]
student_collection = database["students"]

# Function to retrieve the collection
def get_student_collection():
    return student_collection
