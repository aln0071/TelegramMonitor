# TelegramMonitor

This is a Python 3.8 script that monitors a Telegram group.

## What it does

1) Listen for new messages in a group
2) If new message contains a specified substring, then the computer starts beeping for 20 seconds

## Why it is developed

There was a Telegram group that monitors US Visa Interview Slots. People of this group will post a 'GO' message when they find it. I had to monitor this group continuously to see if there is a 'GO' message, which was tiresome. So, I created this program, which will monitor the group and then beep when there is 'GO' message.

### Background

I developed this program during October 2020. It was when the US Consulate was releasing very limited number of visa interview slots due to COVID. They released around 30 to 100 slots per day and these slots would get filled up within 1 minute. I could not continuously monitor their website as it will lock the account for 72 hours if anyone trys to login more than 3 times in a single day. And there was also timeout for each session which was around 30 minutes. Booking a slot became very defficult. Then I came to know about a Telegram group that was operated by students like me who wanted to book slots. They had an excel sheet in which each day is divided into 10 minute slots. Each member of the group must take up at least one slot each day. So, during your time slot, you will have to login with your account and update in the Telegram group if interview slots are available. The codes used were
> NA - Not Available  
> NAOG - Not Available from Other Group  
> GO - Slots are available  
> NABB - No Blue Box
  
If you want to know what a bluebox is, then please go to my repository named [Bluebox](https://github.com/aln0071/Bluebox) which describes what it is. I am not explaining it here as it will be redundant.

The core concept is that I will have to always look for the GO message in the Telegram group and then login and try booking a slot if anyone puts a GO message. For the first couple of days, I monitored the group manually. But after that, I became very stressed out as I had to monitor it all the time. I was not even getting enough sleep as slots could be released at any time. My friend also had the same issue. So, I created this program which will monitor the group for us and beep if there is a GO message.

## How can you use this program

I created a newer version of this program in 2024 (monitor_v2.py). The below setup is for using the older version (monitor_v1.py). Scroll down to see details about the newer version.

1) Go to https://my.telegram.org/auth?to=apps to register a new Telegram desktop application
2) After registration, you will get an API ID and API hash. Copy these values and set it to the api_id and api_hash variables in the program.
3) Get the group's joining link (a string) or channel id (a number) and set it to variable channel_id in the program.
4) Change the substring from 'go' to whatever you want by changing the substring variable. The program will beep when a message having the specified substring appears.
4) Save and start the program with ``` python monitor.py ```

## New Version (monitor_v2.py)

As I had to get a slot again in 2024, I upgraded the program to create monitor_v2.py. This newer version has error handling to enable auto-reconnect, config file to modify behavior, option to accept user input, and multithreading. I had set this up on my Android Phone, and this could be setup on iOS as well. But I will explain the setup for Android.

1) Go to https://my.telegram.org/auth?to=apps to register a new Telegram desktop application
2) After registration, you will get an API ID and API hash. Copy these values and set this in the config.json file.
3) Add the link to all the Telegram groups you like to monitor inside the ```channels``` array in config.json. You can add multiple groups as ```,``` separated strings.
4) Copy over both config.json and monitor_v2.py to your Android device.
5) From playstore, install Termux terminal emulator.
6) Run the following commands to install python and telethon:
```
pkg install python
pip install telethon
```
7) Run the script by ```python monitor_v2.py```
8) Follow the onscreen instructions to sign in.

Once signed in, you are all set. For iOS, use a similar terminal emulator.
