import geocoder
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

logo=(red+"""

 __          ___    _ _____ _______ ______ 
 \ \        / / |  | |_   _|__   __|  ____|
  \ \  /\  / /| |__| | | |    | |  | |__   
   \ \/  \/ / |  __  | | |    | |  |  __|  
    \  /\  /  | |  | |_| |_   | |  | |____ 
     \/  \/   |_|  |_|_____|  |_|  |______|
                                           
                                           
""")
logo2=(green+"""

______ _____    _____ _     
|  _  \  ___|  |_   _| |    
| | | | |____   _| | | |    
| | | |  __\ \ / / | | |    
| |/ /| |___\ V /| |_| |____
|___/ \____/ \_/\___/\_____/
                            
                            
""")

print(logo+logo2)

print(purple+"                     LOGIN PANAL ©©©©©")






usern="white"
passwd="devil"


inpuser=str(input("       Enter Your username>>> "))
inppass=str(input("       Enter Your password >>> "))

if usern==inpuser and passwd== inppass:
	print("{√} username & password correct!")
	pass
else:
	print("{x}username & password wrong!!")
	sys.exit()

ip = geocoder.ip("")

ip = geocoder.ip("me")
logo=(red+"""

 __          ___    _ _____ _______ ______ 
 \ \        / / |  | |_   _|__   __|  ____|
  \ \  /\  / /| |__| | | |    | |  | |__   
   \ \/  \/ / |  __  | | |    | |  |  __|  
    \  /\  /  | |  | |_| |_   | |  | |____ 
     \/  \/   |_|  |_|_____|  |_|  |______|
                                           
                                           
""")
logo2=(green+"""

______ _____    _____ _     
|  _  \  ___|  |_   _| |    
| | | | |____   _| | | |    
| | | |  __\ \ / / | | |    
| |/ /| |___\ V /| |_| |____
|___/ \____/ \_/\___/\_____/
                            
                            
""")
print(logo+logo2)
print("            ===============================================                     ©©©WELCOME TO WHITE DEVIL TOOL©©©                     DeVoloper BY >>>} arnov_chowdhury             ===========================================    ")
inpip=str(input(yellow+"Enter your target IP >>>>"))
print(ip.city)

print(ip.latlng)

location = ip.latlng

