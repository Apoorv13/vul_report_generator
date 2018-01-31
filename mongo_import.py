from pymongo import MongoClient
import itertools

client = MongoClient('localhost', 27017)
db = client['report_helper']
collection = db['vulnerability']


vul_finding = ['Sensitive Information in URL','Application is vulnerable to MITM attack','Android Backup is set to true','Application uses weak hashing algorithm']
vul_desc = ['It was observed that the web application uses the GET method to process requests that contain sensitive information like user session token which is generated after valid authentication','It was observed that the application doesnot implement SSL securely. Trusting all the certificates or self signed certificates is a critical security hole.', 'While performing static analysis of the android APK, it was observed that the application allows to perform backup. The android:allowBackup was set to "true" in the AndroidManifest.xml file.', '"It was observed that the application uses weak hashing algorithm.']
vul_crit = ['Medium','Medium','Low','Low']
vul__risk = ['Sensitive information like user token, can be exposed through the browser\'s history, Referers, web logs, and other sources. Successful exploitation of query string parameter vulnerabilities could lead to an attacker impersonating a legitimate user, obtaining proprietary data, or simply executing actions not intended by the application developers.','The vulnerability will allow an attacker to MITM the application traffic','The ADB provides users a mechanism for attaching their phone to a PC or other device and issuing commands. This includes backup and restore functionality, which allows the user to copy data from the phone to the PC and vice versa, including data contained in internal storage. If the backup contains any sensitive user information, there might be a possibility of it getting leaked to the unintended sources in case of unauthorized access to the backup file.','MD5 is a weak hash known to have hash collisions. .']
vul_recom =['It is recommended not to write any senitive information to disk.','Use secure cryptographic algorithms to perform encryption','"If the application holds sensitive data, it is possible to prevent the users from making a backup of the application. It is recommended that the following line in the AndroidManifest.xml file \nandroid:allowBackup=false is configured.']

#for (a, b, c, d, e) in zip(vul_finding, vul_crit, vul_desc, vul__risk, vul_recom):
#     print a, b, c, d , e
 
print "\niterating using izip"
for (a, b, c, d ,e ) in itertools.izip(vul_finding, vul_crit, vul_desc, vul__risk, vul_recom):
    dictionary_import = { 
        'vul_finding' : a,
        'vul_crit' : b, 
        'vul_desc' : c, 
        'vul__risk' : d, 
        'vul_recom' : e
    }
    collection.insert(dictionary_import)