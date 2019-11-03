import re
import smtplib
import dns.resolver

# Address used for SMTP MAIL FROM command  

def email_verificator(email):
    fromAddress = 'ebbryl.tyut@gmail.com'
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    # regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    try:

        # Email address to verify
        # inputAddress = input('Please enter the emailAddress to verify:')
        inputAddress = email
        addressToVerify = str(inputAddress)

        #validator
        check = True
        temp2 = ''

        # Syntax check
        match = re.match(regex, addressToVerify)
        if match == None:
            check = False

        if check == True:
            splitAddress = addressToVerify.split('@')
            domain = str(splitAddress[1])
            records = dns.resolver.query(domain, 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)

            server = smtplib.SMTP()
            server.set_debuglevel(0)

            server.connect(mxRecord)
            server.helo(server.local_hostname)
            server.mail(fromAddress)
            code, message = server.rcpt(str(addressToVerify))
            server.quit()

            print(code)
            print(message)

            # Assume SMTP response 250 is success
            if code == 250:
                temp2 = "Success"

            else:
                temp2 = "Failed"
    except:
        print("error")
        temp2 = ""
    return temp2