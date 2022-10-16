# What happens when you type `https://www.google.com` in your browser and press `Enter`


## DNS Resolution

The first thing that happens when you press the `Enter` key is your web browser starts the process of finding the IP(Internet Protocal) Address of the domain, in our case which is `google.com`, this is useful because as an end user its just easier to remember the domain name rather than some random IP Address. This process is called **DNS Resolution**.  The first place that is searched is cache in the web browser, if the domain is unknown to the browser, the OS (Operating System) checks its DNS cache, if the domain is still unknown, the DNS resolver is next on the chain, its typically your ISP and if the DNS resolver can't find the domain in its cached database, the DNS resolver asks the DNS root server if it has the IP address of `google.com`, if no, the DNS root server provides the location where the **Top Level Domain(TLD)** is found, in this case where the `.com` extension is to be found. 
The next step in the DNS resolution journey querying for `google.com` in the **`.com` TLD**, if the TLD can't find the domain, it atleast provides the authoritative name servers. Since domain names are registered with domain registrars and when that happens they are shared with TLDs. The last step in this journey is querying the nameservers of `google.com` what the IP address is, the nameservers return an IP address which turns out to be `172.217.169.238` at the time of writing. The IP address is cached by the DNS resolver and by the OS and by the browser that asked for it. If the IP address was found at an earlier point in the chain, it is retrieved, that's why it takes longer the first time you search a domain name and not the second time. If the domain was nowhere to be found and the browsers would show a connection error.


## The Request Chain
After the IP address has been found the browser makes an **HTTPS** request to the IP address

### TCP/IP
When the request is made, data is being prepared for transfer and transfered  from client to server or from server to client and in this case over the HTTPS protocol (which is part of the application layer in the OSI Model) which depends on TCP/IP. These protocols are used since they can determine the most efficient path through a network. The data is transfered over the transport layer, which maintains the connection between the client and server, TCP is used for transfer. TCP handles communications between hosts and provides flow control, multiplexing and reliability. When TCP protocol is used it triggers what is called a *3-way handshake** before actual data transfer begins. The data goes through the network layer which is also called the internet layer and goes through the physical layer(cables and modems) as a series of bytes until it later rebuild on the other end.


### The Load Balancer that handles our requests

Typically load balancers are implemented to minimize the load on one individual servers, thus the name, they are an intermidiate layer that pass request to a web server that would actually handle our request. The amount of load handled by a web server depends on the resources it has, its capacity and the amount of load it handling, but there are other alogrithms that can be used besides weighted load balancing, round robin which balances the load by giving each web server a chance to respond to a request until each one has got a chance and the process repeats.



### SSL Certificate Exchange

The request that we made has reached the load balancer, it was made over HTTPS, the 'S' in 'HTTPS' stands for secure. A load balancer is usually also setup to handle SSL(Secure Sockets Layer), the advantage of using SSL is that communication between the client and server would be secured. The way this works by the use of asymmetric encryption, where there are two keys, a public and a private key, for rsa as an example these keys are generated together from large prime numbers. The public key can encrypt data and only the private key can decrypt it and anything encrypted by the private key can be decrypted by the public key and so forth. So what happens in our situation is the private keys are kept safely with google and the public keys are sent to any one who wants to communicate with google, thus no one else can jump in the network and observe our communications with google. If the request had been made over HTTP then a hacker or anyone who has tapped into our line can easily inspect and read our communications in plain text. The load balancer of google would send us an SSL certificate to encrypt our communications and then forwards the communicated data to the web server, if we have already recieved a certificate the load balancer also decrypts encrypted data we have sent using the SSL certificate we recieved and anything that the load balancer receives from the server is encrypted and sent back to us for decryption using the SSL certificate. The encryption/decryption on our end is taken care of by our browser.

### Firewall
The web server and the load balancer communicate data freely without the need for encryption and since the only client the web server would actually communicate with would be the load balancer, it makes sense to block every other incoming traffic except for ports that are needed to communicate with the load balancer. With this method no one else can talk to the web server even if they wanted to unless they have been authorized or is in this case an authorized load balancer. This is basically achieved using a firewall, which filters, allows or blocks traffic from certain IPs and ports. This can be one layer of security which can protect the server from "unneccesary load". Firewalls are installed on the web server and can be used to monitor, allow and reject inbound and outbound traffic.

### Web server
One of googles servers has received our request, which has already been passed by the load balancer decrypted. The web server could be a hardware or a software, it stores server softwares, website components and static pages like html, css stylesheets, javascript files and possibly other documents that make a website work, in our case everything neccessary to make `google.com` work properly without a hitch.

### Application server
The application server handles the business logic and basically needs to have everything to handle your request, so that you get a response that is suited to your needs. The application server normally sits between the database servers and web servers and acts as a bridge to access data from databases and database servers and to give proper resonse to clients.

### Database server
A database server is a program that is installed to easily access data from a database and also feed data in

### Database
A database is a properly sorted and an eaily accessable way of storing data or information
