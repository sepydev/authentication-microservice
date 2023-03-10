import uvicorn
import config_di  # noqa

if __name__ == "__main__":
    uvicorn.run(
        "app.infrastructure.web.endpoints.user_endpoint:api",
        host='0.0.0.0',
        port=4557,
        reload=True,
        debug=True,
        workers=1
    )
