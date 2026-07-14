from pathlib import Path
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (se você estiver rodando localmente)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Puxa a chave secreta do ambiente ou usa a padrão localmente
SECRET_KEY = os.environ.get('SECRET_KEY')

# O DEBUG será True localmente, mas False na Vercel se você configurar a variável DEBUG=False lá
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Mantém liberado para qualquer host (você pode restringir depois para o domínio da Vercel)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise adicionado logo após o SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'doula_malu.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'doula_malu.wsgi.application'


# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
MONGODB_URI = os.environ.get('MONGODB_URI')

if MONGODB_URI:
    # Configuração Produção / Atlas (Djongo)
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'doula_malu_db', # Nome do seu banco de dados no MongoDB
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': MONGODB_URI,
                #'authMechanism': 'SCRAM-SHA-1'
            }
        }
    }
else:
    # Configuração Local (SQLite3)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True

# O USE_TZ deve ser False para evitar que o Djongo quebre ao salvar datas (DateTimeField)
USE_TZ = False 

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin customization
JAZZMIN_SETTINGS = None