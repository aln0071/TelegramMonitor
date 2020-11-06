# TelegramMonitor

This is a Python 3.8 script that monitors a Telegram group.

## What it does

1) Listen for new messages in a group
2) If new message contains a specified substring, then the computer starts beeping for 20 seconds

## Why it is developed

There was a Telegram group that monitors something. People of this group will post a 'GO' message when they find it. I had to monitor this group continuously to see if there is a 'GO' message, which was tiresome. So, I created this program, which will monitor the group and then beep when there is 'GO' message. Thats all I can tell about it now. I will make it more clear within few months.

## How can you use this program

1) Go to https://my.telegram.org/auth?to=apps to register a new telegram desktop application
2) After registration, you will get an API ID and API hash. Copy these values and set it to the api_id and api_hash variables in the program.
3) Get the group's joining link (a string) or channel id (a number) and set it to variable channel_id in the program.
4) Change the substring from 'go' to whatever you want by changing the substring variable. The program will beep when a message having the specified substring appears.
4) Save and start the program with ``` python monitor.py ```