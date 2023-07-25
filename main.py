from pyrogram import Client
from datetime import date
class Subs:
    def __init__(self, api_id, api_hash):
        api_id = api_id
        api_hash = api_hash

        self.app = Client('my_account', api_id, api_hash)
    
    def check_members_count(self, channel_id):
        self.app.start()

        channel_info = self.app.get_chat(channel_id)
        subs = channel_info.members_count

        self.app.stop()
        return subs
    
client = Subs(api_id, api_hash)

channels = ['', '']

for channel in channels:        
    print('Количество подписчиков канала',channel,client.check_members_count(channel),date.today())
