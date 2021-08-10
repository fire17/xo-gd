#howTo.py
'''
sources
http://5.9.10.113/65127212/python3-nat-hole-punching
https://stackoverflow.com/questions/65127212/python3-nat-hole-punching
https://bford.info/pub/net/p2pnat/
https://stackoverflow.com/questions/53479668/how-to-make-2-clients-connect-each-other-directly-after-having-both-connected-a/53553885#53553885
https://stackoverflow.com/questions/23249787/problems-with-tcp-hole-punching
'''

'''
./tcphole_server.py
We have a client. Client advertised his local IP as: 10.10.10.50
Although, our connection is from: [89.22.11.50]:32928
We have a client. Client advertised his local IP as: 192.168.1.20
Although, our connection is from: [78.88.77.66]:51928

./tcphole_client1.py
b'Greetings! This message came from SERVER as message back!'
b'SERVER registered your data. Your local IP is: 192.168.1.20 You are connecting to the server FROM: 89.22.11.50:32928'

./tcphole_client2.py
b'Greetings! This message came from SERVER as message back!'
b'SERVER registered your data. Your local IP is: 10.10.10.50 You are connecting to the server FROM: 78.88.77.66:51928'
'''


'''
Finally found the expected behavior! Don't want to give too much code here but I hope after this you will understand the basics of how to implement it. Best to have a separate file in each of the client's folder - nearby ./tcphole_client1.py and ./tcphole_client2.py. We need to connect fast after we initiated sessions with the SERVER. Now for instance:

./tcphole_client_connector1.py 32928 51928

./tcphole_client_connector2.py 51928 32928
Remember? We need to connect to the same ports as we initiated with SERVER:

[89.22.11.50]:32928 <> [78.88.77.66]:51928
The first port is needed to bind the socket (OUR). With the second port, we are trying to connect to the CLIENT. The other CLIENT doing the same procedure except it binds to his port and connects to yours bound port. If the ROUTER still has an active connection - SUCCESS.

'''
