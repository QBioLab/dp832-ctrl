Control library for Rigol DP832(A). Currently only tested on Linux connected
via USB.

Fork from [hollanderic/dp832](https://github.com/hollanderic/dp832), modify and
expend for laboratory usage.

## Control from web
1. install nginx, fcgiwrap
2. configure ngix with fastcgi at `/etc/nginx/site-aviliable/default`
```bash
location ~ \.cgi$ {
                autoindex on;
                gzip           off;
                root           /var/www/cgi-bin;
                fastcgi_pass   unix:/var/run/fcgiwrap.socket;
                # include      fastcgi_params;
                fastcgi_param  QUERY_STRING       $query_string;
                fastcgi_param  REQUEST_METHOD     $request_method;
                fastcgi_param  CONTENT_TYPE       $content_type;
                fastcgi_param  CONTENT_LENGTH     $content_length;

                fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
                fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
                fastcgi_param  REQUEST_URI        $request_uri;
                fastcgi_param  DOCUMENT_URI       $document_uri;
                fastcgi_param  DOCUMENT_ROOT      $document_root;
                fastcgi_param  SERVER_PROTOCOL    $server_protocol;

                fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
                fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;

                fastcgi_param  REMOTE_ADDR        $remote_addr;
                fastcgi_param  REMOTE_PORT        $remote_port;
                fastcgi_param  SERVER_ADDR        $server_addr;
                fastcgi_param  SERVER_PORT        $server_port;

                # According to RFC3875 (https://tools.ietf.org/html/rfc3875#section-4.1.14) in SERVER_NAME
                # we should put actual hostname user came to. For nginx it is in $host
                # This will allow to run multihost instances
                fastcgi_param  SERVER_NAME        $host;
        }
```

https://wiki.debian.org/nginx/FastCGI
https://zh.wikipedia.org/wiki/%E9%80%9A%E7%94%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3


## Control in Python
Just to copy `dp832.py` to your working folder. Then:
```python
import dp832
# Create python object with power supply's linux path
# you should check it by yourself
dp = dp832.dp832(fname="/dev/usbtmc0")
dp.On(1) # turn on channel 1
dp.On(2) # turn on channel 2
dp.On(3) # turn on channel 3
dp.Off(1) # turn off channel 1
dp.Off(2) # turn off channel 2
dp.Off(3) # turn off channel 3
```
