import smtplib

my_acc = "isolatedman100@gmail.com"
passs = "ovynxjohttoowciq"

# Use SMTP_SSL for a secure connection
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connect:
    try:
        for i in ["samudralakartikeya@gmail.com", "samudralakartikeya0@gmail.com", "svksales9@gmail.com", "srilochan7@gmail.com"]:
            connect.login(user=my_acc, password=passs)

            # Create the email message
            subject = "Hey handsome"
            body = "dude    Wasuuuppp /n i am kartikeya dont u remeber meee replyy asappp"
            message = f"Subject: {subject}\n\n{body}"

            # Send the email
            connect.sendmail(from_addr=my_acc, to_addrs=i, msg=message)

            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"Error: {e}")
