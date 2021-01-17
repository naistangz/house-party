from decouple import config
from music_controller import settings

CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET
# REDIRECT_URI = "http://127.0.0.1:4000/spotify/redirect"
REDIRECT_URI = settings.REDIRECT_URI
