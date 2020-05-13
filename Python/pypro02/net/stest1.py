#socket 통신 확인
import socket
print(socket.getservbyname('http', 'tcp'))     #80
print(socket.getservbyname('telnet', 'tcp'))  #23
print(socket.getservbyname('ftp', 'tcp'))      #21

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
#[(<AddressFamily.AF_INET: 2>, 0, 6, '', ('210.89.164.90', 80)), (<AddressFamily.AF_INET: 2>, 0, 6, '', ('210.89.160.88', 80))]