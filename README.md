# ActivityPunk

A command-line tool for participating in the fediverse without a server. 

You will need a way to host flat files and a way to receive POST requests but I use a lambda for this with no web server.

## Set up

Pre-requisites:

This project assumes you have a place to host static HTTP files and a way to listen for POST requests, storing the headers and body to a flat file. I will use AWS s3 for hosting static files and AWS Lambda with an API Gateway to listen for POSTs and write them to s3.

Install with pip:

```
```

Create a config file at `~/.activitypunk/config` that defines your identity. For example, mine looks like this:


```ini
[default]
user_at_host = jake@jakekara.com
actor = https://jakekara@jakekara.com
private_key_file = ~/.activitypunk/private.pem
public_key_file = ~/.activitypunk/public.pem
s3_bucket = activitypub
local_data = ~/.activitypunk/data
```

## Use cron to autosync

```shell
# Run at the 18th minute every hour
18 * * * * apunk inbox --sync >> ~/.activitypunk/synclog.txt
```