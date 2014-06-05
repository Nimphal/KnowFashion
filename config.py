import os


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
BASE_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
UPLOADS_FOLDER = os.path.join(BASE_FILE_PATH, 'app', 'static', 'uploads')
DEFAULT_FILE_STORAGE = 'filesystem'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
