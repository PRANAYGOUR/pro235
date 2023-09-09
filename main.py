import requests 
for i in range(1,100):
    URL = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    #https://www.amazon.in/gp/css/homepage.html?ref_=nav_AccountFlyout_ya
    r = requests.get(url=URL)
    if r.status_code==200:
        print(URL)
    