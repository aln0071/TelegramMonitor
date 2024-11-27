from telethon import TelegramClient, events
import time
import os
import threading
import asyncio
import json

with open('config.json', 'r') as file:
    config = json.load(file)

api_id = config['apiId']
api_hash = config['apiHash']
channel_id = config['channels']
substring = "na"

client = TelegramClient('anon', api_id, api_hash)

sound_loop_length = config['beepCount']

playing_sound = False
stop_playing = False

# Event to signal shutdown
shutdown_event = threading.Event()

def playSound():
    global playing_sound, stop_playing
    if playing_sound:
        return
    playing_sound = True
    loop_count = 0
    while loop_count < sound_loop_length:
        if stop_playing:
            stop_playing = False
            break
        os.system('mpv beep.mp3 > /dev/null 2>&1')
        time.sleep(1)
        loop_count = loop_count + 1
    playing_sound = False

@client.on(events.NewMessage(chats=(channel_id)))
async def event_handler(event):
    t1 = threading.Thread(target=playSound, args=[])
    print("="*20)
    sender = await event.get_sender()
    print('time received: %s' % time.strftime("%H:%M:%S", time.localtime()))
    print('Sender: %s %s' % (sender.first_name, sender.last_name or ''))
    print(event.raw_text)
    if(str(event.raw_text).lower().startswith(substring) != 1):
        print("go message found")
        t1.start()
    else:
        print("not go message")
    print("=" * 20)
    print("\n")

def input_listener():
    global stop_playing, playing_sound, shutdown_event, client
    while True:
        input("Any key to stop sound: \n")
        if playing_sound:
            print("Stopping sound...")
            stop_playing = True

# Start the input listener in another thread
input_thread = threading.Thread(target=input_listener)
input_thread.daemon = True  # Ensures the thread exits when the main program exits
input_thread.start()

# Reconnection logic in case of network failure
async def run_client():
    while True:
        try:
            # Start the client
            await client.start()
            print("Client connected successfully.")
            
            # Keep the client running
            await client.run_until_disconnected()
        except (OSError, asyncio.TimeoutError) as e:
            print(f"Network error occurred: {e}. Reconnecting...")
            await asyncio.sleep(5)  # Wait before attempting to reconnect

loop = asyncio.get_event_loop()
loop.run_until_complete(run_client())