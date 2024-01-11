import smtplib

my_acc = "isolatedman100@gmail.com"
passs = "ovynxjohttoowciq"

# Use SMTP_SSL for a secure connection
connect = smtplib.SMTP("smtp.gmail.com")
connect.login(user=my_acc, password=passs)

    # Create the email message
subject = "Hello from kartikeya"
body = "dude    Wasuuuppp"
message = f"Subject: {subject}\n\n{body}"

    # Send the email
connect.sendmail(from_addr=my_acc, to_addrs="samudralartikeya0@gmail.com", msg=message)

print("Email sent successfully!")
