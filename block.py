import json
import os
import hashlib
from firebase import firebase
import socket 
import smtplib  

firebase = firebase.FirebaseApplication("https://blockchain-a2e11-default-rtdb.firebaseio.com/", None)



def hash_create(prev_block):
    content = json.dumps(prev_block, indent=2).encode('utf-8')
    nonce = 1
    while(1):
        hash = (content.decode('UTF-8') + str(nonce)).encode()
        hash = (hashlib.sha256(hash)).hexdigest()
        print(hash)
        if(hash[:1]=="".zfill(1)):
                
            break
        nonce = nonce + 1
    return hash
def check_integrity():
    all_results = []
    results = firebase.get('blockchain-a2e11-default-rtdb/Blocks','')
    for result in results:
        content = firebase.get('blockchain-a2e11-default-rtdb/Blocks',result)
        # ds = content['prev_block']['filename']
        prev_hash = content.get('prev_block').get('hash')
        prev_filename = content.get('prev_block').get('filename')
        
        hashone = firebase.get('blockchain-a2e11-default-rtdb/Blocks',prev_filename)
        actual_hash = hash_create(hashone)
        
        if prev_hash == actual_hash:
            res = 'OK'
            
        else :
            res = 'was changed'
            # suspicious(ds)
            
        all_results.append({'block' : prev_filename, 'result' : res})
    
    return all_results    
    
# def suspicious(last_file):
#     results = firebase.get('blockchain-a2e11-default-rtdb/Blocks','')
#     for result in results:
#         content = firebase.get('blockchain-a2e11-default-rtdb/Blocks',result)
#         print(content)
#         ds = content['prev_block']['filename']
#         print(ds)
#         suspect = firebase.get('blockchain-a2e11-default-rtdb/Blocks',last_file)
#         emai = suspect['Email']
#     print(emai)
#     hostname=socket.gethostname()   
#     IPAddr=socket.gethostbyname(hostname)   
#     # print("Your Computer Name is:"+hostname)   
#     # print("Your Computer IP Address is:"+IPAddr)   

#     sender_email = 'adjangam9@gmail.com'
#     rec_email = emai
#     password = 'aditya@2002'
#     message = f'''We noticed a new access to your nonce data on a Windows device. 
#     If this was you, you dont need to do anything.
#     hostname is {hostname} and ip address is {IPAddr}, trying to login.'''

#     server = smtplib.SMTP('smtp.gmail.com',587)

#     server.starttls()

#     server.login(sender_email,password)
#     print("Login successfully")
#     server.sendmail(sender_email,rec_email,message)
#     return ("Email hsas been sent to ",rec_email)
    
def write_block(adhar_number, pancard, driving_license,email):
    
    results = firebase.get('blockchain-a2e11-default-rtdb/Blocks','')
    r = list(results.keys())[-1]
    new_results = firebase.get('blockchain-a2e11-default-rtdb/Blocks',r)

    data = {
        "adhar_number" : adhar_number,
        "Pancard" : pancard,
        "Driving License " : driving_license,
        "Email" : email,
        "prev_block" : {
            "hash" : hash_create(new_results),
            "filename" : r
        }
    }
    
    
    writing =  firebase.post('blockchain-a2e11-default-rtdb/Blocks',data)

def main():
    suspicious('-N-2pzRByTxM9zxQgh_W')

if __name__ == '__main__':
    main()