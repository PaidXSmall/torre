import motor.motor_asyncio
from config import DATABASE_NAME, DATABASE_URI

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users


    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

db = Database(DATABASE_URI, DATABASE_NAME)
