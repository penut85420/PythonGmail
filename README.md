# Python Gmail
+ This work contais two parts, the first part is to send email via gmail, and the second part is to use gmail API with credential hidden in environment variable.

## Email Sending via Gmail
+ [Source code](send_mail.py)
+ Using Gamil without 2FA:
    + [Allow Less Secure Apps to Access](https://tinyurl.com/l2uoqm2)
+ (Recommended) Using Gamil with 2FA:
    + [Signing in with an App Password](https://tinyurl.com/ydahwxwv)

## Gmail API using Python
+ Reference: [Gmail API Python Quickstart](https://tinyurl.com/oh2ehm5)
+ This work try to do a hacky way to hide credential into environment variables, the source code is modified from the example code of the tutorial above.
+ [Source code](gmail_api.py)
+ In original work, using `pickle.dump` will make a binary file, and a file named `credential.json` is also need to be under the root of project.
+ In this work, we store whole `credential.json` as a string in `.env` file, and we use `pickle.dumps` to convert the credential object into a `bytes` object, then we use `bytes.hex` to convert the `bytes` object in to a hex string, so we can store this hex string into regular file instead of a binary file.
  + In this case, we store this hex string into `.env` file so the credential can be load as an environment variable.
+ If we want to load the credential, we can use `os.environ['CREDS_HEX']` to get the hex string of the credential object, and convert hex string into `bytes` (which actually `bytearray`) by `bytearray.fromhex`, so the `pickle.loads` can load the credential object from the `bytes` object.

## Playing Bytes
+ [Source code](hex_bytes.py)
+ This script shows how to convert object into hex string and recover the object from hex string.

## Reference
+ StackOverflow
  + [How to create python bytes object from long hex string?](https://stackoverflow.com/a/17160152/4893895)
  + [How to expose Gmail API credentials.json to env](https://stackoverflow.com/a/61886409/4893895)