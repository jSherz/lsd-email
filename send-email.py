#!/usr/bin/env python3

import requests
import htmlmin
import os

mailgun_domain = os.environ['LSD_EMAIL_DOMAIN']
mailgun_api_key = os.environ['LSD_EMAIL_API_KEY']
email_from = os.environ['LSD_EMAIL_FROM']
email_to = os.environ['LSD_EMAIL_TO']

with open('welcome.txt', 'r') as text_file:
    with open('welcome.html', 'r') as html_file:
        text_content = text_file.read()

        # Minify the HTML to prevent automatic linebreaks being added by MailGun
        html_content = htmlmin.minify(html_file.read())

        # Send e-mail
        response = requests.post(
            "https://api.mailgun.net/v3/" + mailgun_domain + "/messages",
            auth=("api", mailgun_api_key),
            data={"from": "Leeds Skydivers <" + email_from + ">",
                  "to": [email_to],
                  "subject": "Hello from Leeds Uni Skydivers!",
                  "text": text_content,
                  "html": html_content})

        print('Status: ' + str(response.status_code))
        print('Response: ' + response.text)
