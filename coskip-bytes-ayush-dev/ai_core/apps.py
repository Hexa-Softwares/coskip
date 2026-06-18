"""Django app configuration for AI Core."""
from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class AiCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_core'
    verbose_name = 'AI Core'
    
    def ready(self):
        """Initialize Vertex AI on app startup."""
        try:
            from ai_core.services.vertex_client import warmup_vertex_ai
            warmup_vertex_ai()
        except ImportError:
            pass
