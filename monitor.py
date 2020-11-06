from telethon import TelegramClient, events
import winsound
import time

api_id = 1234567
api_hash = ''
channel_id = 1234567890 # group identifier - channel id or joining link

client = TelegramClient('PyMon', api_id, api_hash)

@client.on(events.NewMessage(chats=(channel_id)))
async def event_handler(event):
    print("="*20)
    # print('{}'.format(event))
    sender = await event.get_sender()
    # print(sender)
    print('time received: %s' % time.strftime("%H:%M:%S", time.localtime()))
    print('Sender: %s %s' % (sender.first_name, sender.last_name or ''))
    print(event.raw_text)
    if(str(event.raw_text).lower().find('go') != -1):
        print("go message found")
        winsound.Beep(2500, 20000)
    else:
        print("not go message")
    print("=" * 20)
    print("\n")
with client:
    client.start()
    client.run_until_disconnected()