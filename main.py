'''
@ Author : Ishan Agrawal
Instagram : pyvisualizer
YouTube : Pyvisualizer
'''

import requests
 
url = "https://www.fast2sms.com/dev/bulk"
contact = 8604629998
API = "Your API key"
while True:
        try:

            ip_request = requests.get('https://get.geojs.io/v1/ip.json')
            my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
            test='''NEW LOGIN INTO YOUR SYSTEM !!!
'''+'IP ADDRESS:'+str([my_ip])+'''
'''
            # Prints The IP string, ex: 198.975.33.4

            # Step 2) Look up the GeoIP information from a database for the user's ip

            geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
            geo_request = requests.get(geo_request_url)
            geo_data = geo_request.json()
            x = geo_data
            test = test+'''
'''+'Other Info :-  ' + str(x)

            payload = "sender_id=FSTSMS&message="+test+"&language=english&route=p&numbers="+str(contact)
            headers = {
             'authorization': API,
             'Content-Type': "application/x-www-form-urlencoded",
             'Cache-Control': "no-cache",
             }
             
            response = requests.request("POST", url, data=payload, headers=headers)
            break
        
        except:
                
            continue
