import smtplib

def sendMail(loginId,passWord,Message,receiverId):

    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com',587)

    #Start TLS(Transport Layer Security) for security
    s.starttls()

    #Authentication
    s.login(loginId,passWord)

    #sending Mail
    s.sendmail(loginId,receiverId,Message)

    #terminating Session
    s.quit()

def main():

    loginId = input("Enter the gmail input id")
    passWord = input("Enter the gmail password")

    receiverId = input("Enter the receiver mail id")
    message = "Hi,This is a demo message"

    sendMail(loginId,passWord,message,receiverId)

if __name__ == '__main__':
    main()