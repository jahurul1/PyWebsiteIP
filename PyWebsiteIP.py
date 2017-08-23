import socket
import tldextract

hostname = raw_input('Please enter the URL: ')

list = tldextract.extract(hostname)
 
domain_name = list.domain + '.' + list.suffix


addr = socket.gethostbyname(domain_name)
print 'The IP address of '+ domain_name +' is '+ addr