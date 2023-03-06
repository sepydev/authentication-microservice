import uvicorn
import config  # noqa

if __name__ == "__main__":
    uvicorn.run(
        "app.infrastructure:web.endpoint.user_endpoint",
        host='0.0.0.0',
        port=4557,
        reload=True,
        debug=True,
        workers=1
    )
