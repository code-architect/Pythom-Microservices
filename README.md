###Docker file details
<hr>

To build the image:
```docker build --tag flask-micro .```

To see the image:
```docker images```

To create a container:
```docker run --p 5000:5000 flask-micro```

###User Microservices details
<hr>

####<i>User API End Points</i>

1. ```/api/user/all - GET``` [Going to return list of all users]
2. ```/api/user/create - POST``` [Going to create a user]
3. ```/api/user/login - POST``` [Login the user]
4. ```/api/user/logout - POST``` [Logout the user]
5. ```/api/user/<username>/exists - GET``` [Check if user exists or not]
6. ```/api/user/ - GET``` [Details about currently logged in user]












<i><b>We need to create different venv for each project, for being lazy i am creating one</b></i>