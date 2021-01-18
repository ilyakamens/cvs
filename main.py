#!/usr/bin/env python

from datetime import datetime
import os
import time

from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

def check_and_alert(i):
    resp = requests.get("https://www.ruhealth.org/covid-19-vaccine")
    soup = BeautifulSoup(resp.content, features="html.parser")
    for tr in soup.tbody.findChildren("tr")[3:-2]:
        if not tr.find("a", {"href": "/sites/default/files/covid-19/Full.png"}):
            print(f"Iteration {i}: VACCINE OPENINGS at {datetime.now()}")
            client.messages.create(
                to="+12032741497", from_="+12017204187", body="Check the COVID vaccine website!!!"
            )
            break
    else:
        print(f"Iteration {i}: NO vaccine openings at {datetime.now()}")

if __name__ == "__main__":
    i = 1
    while True:
        try:
            check_and_alert(i)
        except Exception as e:
            print(e)
        i += 1
        time.sleep(5)
