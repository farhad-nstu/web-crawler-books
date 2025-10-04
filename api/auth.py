from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from fastapi.openapi.models import APIKey as APIKeyModel, APIKeyIn
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "default-key")
API_KEY_NAME = "X-API-Key"

# Security scheme for Swagger docs
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate API KEY",
    )

# Swagger docs support
def get_openapi_security_scheme():
    return {
        "apiKeyAuth": {
            "type": "apiKey",
            "name": API_KEY_NAME,
            "in": APIKeyIn.header.value,
        }
    }
