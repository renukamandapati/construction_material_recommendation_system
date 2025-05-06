DB_HOST = 'localhost'  # Change if your MySQL is hosted elsewhere
DB_NAME = 'ConstructionDB'  # Your database name
DB_USER = 'root'  # Your MySQL username (default is 'root')
DB_PASSWORD = 'root'  # Your MySQL password (change if different)

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Your generated JWT secret key
JWT_SECRET_KEY = 'dbd5d4d1d80019e592d4a578af5b511e3aa2fa0323751e58d66f9c29fa3711d2'
