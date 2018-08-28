# Dover
The app(web) allows one to upload a list of urls in csv(comma seperated values) format and after processing, download some information(mentioned below) about the relative lookalike domains in csv format. 

Output Information 
------------
- Domain name
- Creation date
- Expiration date
- Registrar ID
- Location
- Registrar IP

Requirements
------------
**Flask**

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools of libraries.

```
$ pip install flask
```
**Py-whois**

Python module/library for retrieving WHOIS information of domains.

```
$ pip install python-whois
```
Usage
------------
STEP 1 : Clone/Download the repository.

```
$ git clone https://github.com/KeerthiVasan23/Dover.git
```

STEP 2 : Install python-whois and flask.

STEP 3 : Run app.py.

```
$ python app.py
```
STEP 4 : Go to the url in your browser(Default: 127.0.0.1:4444).


STEP 5 : Browse and upload the csv files containing urls.

STEP 6 : Click download to get the output information in csv format.

