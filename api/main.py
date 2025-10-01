from fastapi import FastAPI, Request
from .routes import router
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from .auth import get_openapi_security_scheme
from fastapi.openapi.utils import get_openapi

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Books API", version="1.0.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(router, prefix="/api")

# Apply global rate limit (100 requests per minute per IP)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return {"msg": "Books API is running"}

# Custom OpenAPI schema with API Key support
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="API for Books Scraper with API Key Authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = get_openapi_security_scheme()
    openapi_schema["security"] = [{"apiKeyAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
