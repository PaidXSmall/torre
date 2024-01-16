import re, os
from os import environ


API_ID = "10261086"
API_HASH = "9195dc0591fbdb22b5711bcd1f437dab"
BOT_TOKEN = "6755712881:AAFOEHywraPVcnRrIJyoN5R6jAyDf-a7T6M"
PICS = (environ.get('PICS', 'https://graph.org/file/d23700d1a37c270298028.jpg https://graph.org/file/1f386b0d9e4b19f9c8fac.jpg https://graph.org/file/42c8d2acde7a94dda0336.jpg https://graph.org/file/044ae5927da90e33a593a.jpg https://graph.org/file/1dc7d041f0c7dbb13bc0e.jpg https://graph.org/file/6a03ecc404907e85be5a6.jpg https://graph.org/file/2f713de34b042826faa57.jpg https://graph.org/file/be8d4387c3ff1af07f523.jpg https://graph.org/file/d1efc28c510c4f08206aa.jpg https://graph.org/file/6ff6a7e77ace56f1c59bc.jpg https://graph.org/file/dbb9787d049efb885a61b.jpg https://graph.org/file/dcf4f6bba19afb2816eb9.jpg https://graph.org/file/8a183a4ae75b2284744c3.jpg https://graph.org/file/efdcd11e5905f704bd590.jpg https://graph.org/file/6b9f31026bfa09e8fe687.jpg https://graph.org/file/af0ee87cf3ef99119e1bd.jpg https://graph.org/file/599694cfb3da24e775195.jpg')).split()
TMVPICS = (environ.get('TMVPICS', 'https://graph.org/file/9b70c680c01d4a82e29cb.jpg')).split()
FORCE_SUB   = os.environ.get("FORCE_SUB", "OMGxBotz") 

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://omg:omg@cluster0.cub5z0e.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "omg")
