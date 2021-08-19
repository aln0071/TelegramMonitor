# TelegramMonitor

This is a Python 3.8 script that monitors a Telegram group.

## What it does

1) Listen for new messages in a group
2) If new message contains a specified substring, then the computer starts beeping for 20 seconds

## Why it is developed

There was a Telegram group that monitors US Visa Interview Slots. People of this group will post a 'GO' message when they find it. I had to monitor this group continuously to see if there is a 'GO' message, which was tiresome. So, I created this program, which will monitor the group and then beep when there is 'GO' message.

### Background

I developed this program during October 2020. It was when the US Consulate was releasing very limited number of visa interview slots. They released around 30 to 100 slots per day and these slots would get filled up within 1 minute. I could not continuously monitor their website as it will lock the account for 72 hours if anyone trys to login more than 3 times in a single day. And there was also timeout for each session which was around 30 minutes. Booking a slot became very defficult. Then I came to know about a Telegram group that was operated by students like me who wanted to book slots. They had an excel sheet in which each day is divided into 10 minute slots. Each member of the group must take up at least one slot each day. So, during your time slot, you will have to login with your account and update in the Telegram group if interview slots are available. The codes used were
> NA - Not Available  
> NAOG - Not Available from Other Group  
> GO - Slots are available  
> NABB - No Blue Box
  
If you want to know what a bluebox is, then please go to my repository named [Bluebox](https://github.com/aln0071/Bluebox) which describes what it is. I am not explaining it here as it will be redundant.

The core concept is that I will have to always look for the GO message in the Telegram group and then login and try booking a slot if anyone puts a GO message. For the first couple of days, I monitored the group manually. But after that, I became very stressed out as I had to monitor it all the time. I was not even getting enough sleep as slots could be released at any time. My friend also had the same issue. So, I created this program which will monitor the group for us and beep if there is a GO message.

## How can you use this program

1) Go to https://my.telegram.org/auth?to=apps to register a new Telegram desktop application
2) After registration, you will get an API ID and API hash. Copy these values and set it to the api_id and api_hash variables in the program.
3) Get the group's joining link (a string) or channel id (a number) and set it to variable channel_id in the program.
4) Change the substring from 'go' to whatever you want by changing the substring variable. The program will beep when a message having the specified substring appears.
4) Save and start the program with ``` python monitor.py ```
