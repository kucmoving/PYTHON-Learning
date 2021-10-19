##要降低GOOGLE 安全度> security> off 2 step, off phone sign, allow less secure app access
import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "abcd1345()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr = my_email,
        to_addrs = "appbewerttesting@yahoo.com",
        msg = "Subject:Hello\n\nThis is the body of my email."
    )

##Smtp port
##- Gmail: smtp.gmail.com
##- Hotmail: smtp.live.com
## Outlook: outlook.office365.com
##Yahoo: smtp.mail.yahoo.com

##授權存取
##- https: // accounts.google.com / b / 0 / DisplayUnlockCaptcha
##- 要加入smtplib.SMTP("smtp.gmail.com", port=587)

