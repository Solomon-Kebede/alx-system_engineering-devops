# 0x1B. Web stack debugging #4

## Task 0. Sky is the limit, let's bring that limit higher

**The Task:** In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

**The Solution**

### Installing Apache bench

**Step 1 − Update package database.**
```sh
# apt-get update
```
Please note that symbol # before a terminal command means that root user is issuing that command.

**Step 2 − Install apache2 utils package to get access to Apache Bench.**
```sh
# apt-get install apache2-utils
```
Apache Bench is now installed. If you want to test a web application hosted on the same VPS, then it is enough to install the Apache web server only −
```sh
# apt-get install apache2
```
Being an Apache utility, Apache Bench is automatically installed on installation of the Apache web server.
Verifying Apache Bench Installation

Let us now see how to verify Apache Bench Installation. The following code will help verify the installation −
```sh
# ab -V
```
**Output**
```
This is ApacheBench, Version 2.3 <$Revision: 1604373 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```


## Install curl

```sh
# apt install curl
```

# Testing the capacity of our servers

For a complete guide use this [Reference](https://www.tutorialspoint.com/apache_bench/apache_bench_quick_guide.htm)

**Test 1**

```sh
root@984e03549a14:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   2.610 seconds
Complete requests:      2000
Failed requests:        564
   (Connect: 0, Receive: 0, Length: 564, Exceptions: 0)
Non-2xx responses:      1436
Total transferred:      1013848 bytes
HTML transferred:       633804 bytes
Requests per second:    766.15 [#/sec] (mean)
Time per request:       130.523 [ms] (mean)
Time per request:       1.305 [ms] (mean, across all concurrent requests)
Transfer rate:          379.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2  13.9      0      94
Processing:     1  127  49.7    102     204
Waiting:        1  125  49.2    102     203
Total:          3  129  50.4    103     204

Percentage of the requests served within a certain time (ms)
  50%    103
  66%    109
  75%    194
  80%    196
  90%    197
  95%    198
  98%    201
  99%    202
 100%    204 (longest request)
root@984e03549a14:/#
```


From the reference on `Failed Rrequests`

**Failed Requests** − The number of requests that were considered a failure. If the number is greater than zero, another line will be printed showing the number of requests that failed due to connecting, reading, incorrect content length, or exceptions.

So from the above we can deduce our server failed due to `incorrect content length`

**Test 2**

```sh
# ab -c 100 -n 2000 -v 2 localhost/`
```
Result of a failed response

```
WARNING: Response code not 2xx (500)
LOG: header received:
HTTP/1.1 500 Internal Server Error
Server: nginx/1.4.6 (Ubuntu)
Date: Thu, 10 Nov 2022 16:41:18 GMT
Content-Type: text/html
Content-Length: 201
Connection: close

<html>
<head><title>500 Internal Server Error</title></head>
<body bgcolor="white">
<center><h1>500 Internal Server Error</h1></center>
<hr><center>nginx/1.4.6 (Ubuntu)</center>
</body>
</html>

WARNING: Response code not 2xx (500)
```

With a hypothsis that the server was failing because the server was not able to serve the load that was coming in, I went to check the nginx config file located in `/etc/nginx/nginx.conf`, opening the file in `vi`, I saw on the second line:
```
worker_processes 4;
```

and changed it to different numbers: 40, 2000 and finally to 100

I restarted my nginx server using: `service nginx restart` and I conducted `Test 3`

**Test 3**

```sh
root@984e03549a14:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.227 seconds
Complete requests:      2000
Failed requests:        0
Non-2xx responses:      2000
Total transferred:      742000 bytes
HTML transferred:       402000 bytes
Requests per second:    619.77 [#/sec] (mean)
Time per request:       161.349 [ms] (mean)
Time per request:       1.613 [ms] (mean, across all concurrent requests)
Transfer rate:          224.55 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   4.2      0      94
Processing:     2  160  86.5    117     497
Waiting:        2  160  86.5    117     497
Total:          7  160  86.3    119     497

Percentage of the requests served within a certain time (ms)
  50%    119
  66%    197
  75%    197
  80%    197
  90%    198
  95%    403
  98%    494
  99%    497
 100%    497 (longest request)
root@984e03549a14:/# 
```

As we can see in the above it succeeded without errors, but apache bench was freezing on my end, I assume because of the number of workers, so I decided to incrementally come upto a number of workers that worked without using many workers, so luckilly I started with 10 workers and restarted my nginx server and I got this response

**Test 4**

```sh
root@984e03549a14:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   2.984 seconds
Complete requests:      2000
Failed requests:        0
Non-2xx responses:      2000
Total transferred:      742000 bytes
HTML transferred:       402000 bytes
Requests per second:    670.30 [#/sec] (mean)
Time per request:       149.188 [ms] (mean)
Time per request:       1.492 [ms] (mean, across all concurrent requests)
Transfer rate:          242.85 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   3.0      0      94
Processing:     1  145  50.4    104     200
Waiting:        1  144  50.4    104     200
Total:          3  145  50.3    104     200

Percentage of the requests served within a certain time (ms)
  50%    104
  66%    196
  75%    197
  80%    197
  90%    198
  95%    198
  98%    199
  99%    199
 100%    200 (longest request)
root@984e03549a14:/#
```
As compared to `Test 3` with a total time of `3.227 seconds` , `Test 4` takes less time with a total time of `2.984 seconds`