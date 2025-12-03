import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

# Vercel ke liye
app = application
handler = application  # ← Yeh extra add karo agar logs mein handler error aaye