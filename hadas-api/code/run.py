from app import app
from database import create_tables

def main():
    create_tables()
    app.run(debug=True, port=8000)

if __name__ == '__main__':
    main()