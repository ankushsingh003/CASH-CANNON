import sys
import os

# Ensure the root directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from WEB.app import app

if __name__ == "__main__":
    app.run()
