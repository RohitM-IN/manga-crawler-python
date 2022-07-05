##################
# FOR PRODUCTION
####################
from src.app import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    app.run(host='0.0.0.0', debug=True)