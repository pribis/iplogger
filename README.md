# iplogger
## Give a running tally of ip addresses from the access.log. 

There are only a couple of settings you need to worry about.

1. access_log: The location of the access log you wish to monitor.
2. flush_limit: The number of addresses you wish to store in memory.
   At the limit, the array will simply get deleted and start over. Brutal.
3. The ignore file. Place a file named 'ignore' in the same directory as iplogger
   and populate it with IP addresses, one per line.
   
That is pretty much it. Like everything in life, this is a "use at your own risk"
program.
