# `0x0F. Load balancer` project:

This directory of files for the 0x0F. Load balancer project
All the files and directory is described here
If any file or directory that is not described may be for testing purposes


`0-custom_http_response_header` -> a bash script that configures a brand new Ubuntu machine to the requirements:

- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
	- The name of the custom HTTP header must be X-Served-By
	- The value of the custom HTTP header must be the hostname of the server Nginx is running on


`1-install_load_balancer` -> a bash script that configures a brand new Ubuntu machine to the requirements:
- Configure HAproxy so that it send traffic to web-01 and web-02
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script

