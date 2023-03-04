from app import create_app

app = create_app()

if __name__ == '__main__':
    from uvicorn import run

    run(app, host='0.0.0.0')
