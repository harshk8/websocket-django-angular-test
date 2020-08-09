# websocket-django-angular-test

All the basic details about the application is listed inside the Medium post. 

https://medium.com/@harshkhatke8/web-socket-django-angular-real-time-notification-88caa589d1f6

Below are few steps how we can achieve push notification/ real-time notification functionality. 
Very very basic way to understand how the real time notification can we achieve by using web-socket is explain below in few points and detail next to it:

1. Web-socket provides a consistent connection between client and server. where client is the end user, this connection can be maintain till user is live on site.
2. Web-socket uses the regular HTTP request to the server, which result a web-socket handshake as success response.
3. Once the web-socket handshake success client & server both are able so send data to each other without any disturbance.
4. On success of request a channel creates with a unique name. We can also create a group and add multiple channels init and send signal to groups.
5. In web-socket handshake process here we need an another server which can temporarily store the real-time send & received data. We need separate server because we want to catch data real time without hitting the server to get it. Using that unique channel name or group name we can identify our message.
6. The Redis server will run on a Seperate port, which will broadcast/send the message to the client whenever the connection get new message to release.
