import motor.motor_asyncio
from info import DATABASE_URL

class JoinReqs:

    def __init__(self):
        if DATABASE_URL:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
            self.db = self.client["JoinReqs"]
            self.col = self.db["channel"]
        else:
            self.client = None
            self.db = None
            self.col = None

    def isActive(self):
        if self.client is not None:
            return True
        else:
            return False

    async def add_user(self, user_id, chat_id):
        try:
            await self.col.insert_one({"user_id": int(user_id), "chat_id": int(chat_id)})
        except:
            pass

    async def get_user(self, user_id):
        channels = await self.col.find_one({"user_id": int(user_id)})
        return channels

    async def get_all_users(self):
        return await self.col.find().to_list(None)

    async def delete_user(self, user_id):
        await self.col.delete_one({"user_id": int(user_id)})

    async def delete_all_users(self):
        await self.col.delete_many({})

    async def get_all_users_count(self):
        return await self.col.count_documents({})
