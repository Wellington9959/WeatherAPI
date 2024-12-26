from src.configuration import settings
from src.setup import create_application

app = create_application(settings=settings)

if __name__ == "__main__":
    app.run()
