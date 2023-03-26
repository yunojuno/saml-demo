from .base import *  # noqa: F403

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".ngrok.io"]

DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": "demo.db"}

if not SOCIAL_AUTH_SAML_SP_PUBLIC_CERT:
    with open("saml.crt") as f:
        SOCIAL_AUTH_SAML_SP_PUBLIC_CERT = f.read()

if not SOCIAL_AUTH_SAML_SP_PRIVATE_KEY:
    with open("saml.key") as f:
        SOCIAL_AUTH_SAML_SP_PRIVATE_KEY = f.read()


# Ensures that the request is secure when running behind a proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
