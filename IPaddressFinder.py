# knowing the IP address of a website 
import socket


print("  ::This is a IP address finder of any website you want:: ")
print("\n\n")
print("  Please make sure that your internet is on. :)")
print("\n\n")
# Taking the server name
host = str(input("  Enter the complete website : "))
print("\n")
try:
    # know the IP address of the website
    addr = socket.gethostbyname(host)
    print("  IP Address of the website = " + addr)

except socket.gaierror:     #if get address info error occurs
    print("  The Website does not exist.")

input("\n\n\n\n   Press enter to exit.")
