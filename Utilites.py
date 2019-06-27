from pyodbc import connect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def connecttosqlserver(servername,databasename,query):

    connection = connect('Driver={SQL Server};'
                         'Server=servername;'
                         'Database=databasename;'
                         'Trusted_Connection=yes;')

    cursor = connection.cursor()
    cursor.execute(query)
    dataCollection = []
    for row in cursor:
        dataCollection.append(row)
    cursor.close()
    connection.close()
    return dataCollection

def createsmtpconnection(hostname,port,emailaddress,password):
    smtpobject = smtplib.SMTP(host=hostname, port=port)
    smtpobject.starttls()
    smtpobject.login(emailaddress,password)
    return smtpobject


def sendmail(smtpobject,toid,fromid,subject,message):
    msg = MIMEMultipart('alternative')
    msg["Subject"] = subject
    msg['From'] = fromid
    msg['To'] = toid
    part1 = MIMEText(message, 'html')
    msg.attach(part1)
    smtpobject.sendmail(fromid, toid, msg.as_string())
    smtpobject.quit()
