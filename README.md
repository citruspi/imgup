## imgup

imgup is a tiny web application which lets you

- upload image files
- get a URL for embedding uploaded images

It does not:

- convert files
- let you see previously uploaded files
- delete files
- support multiple user accounts
- have titles or captions
- group images into albums

You drag and drop an image, get a URL, and use it. Nothing fancy.

## Quick Start

The only dependency is `flask`...

```
$ pip install flask
```

The default password included is `pancake`, but you probably want to change that.

```
$ python
Python 2.7.5 (default, Aug 25 2013, 00:04:04)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hashlib
>>> hashlib.sha512('PASSWORD').hexdigest()
'DIGEST'
>>> quit()
```

Replace `PASSWORD` with the password of your choice and save the `DIGEST` to `config.py`.

Run the application with

```
$ python app.py
```

## Screenshots

#### "Login" Page

![](http://i.imgur.com/42qMHwa.png)

#### Upload Page

![](http://i.imgur.com/Ni3el6v.png)

#### Successful Upload

![](http://i.imgur.com/chiRy0a.png)

## Configuration

You can edit `config.py` to change

- the port
- the host
- the upload directory
- the file extensions which are allowed
