# PDF2PNG sandbox

Web app provides you with the following:

1. User login/logout
2. Ability to upload PDF files for logged-in users. All users can observe uploaded files.
First column is user's name; Second one is a filename available for downloading.
3. When a PDF is uploaded it is being split into PNG page by page. Each page is also available for downloading alongside with base PDF file.

# Requirements

- Python3
- Tornado
- SQLite

# Deploy

- Clone code
- Install dependencies: `pip3 install -r requirements.txt`
- Fire DB migrations:

```
$ python3
>>> from app import *
>>> seed_db()
```

- Start the service `python3 app.py`
- Check the magic at the `http://127.0.0.1:8888` using `admin / 123456` credentials

