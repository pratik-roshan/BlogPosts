# Flask Blog API

This is a simple Flask application that provides an API for managing blog posts. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

## Getting Started

### Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- PostgreSQL database server

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-blog-api.git
   ```

2. Navigate to the project directory:
  ```sh
  cd Blog
```

3. Create and activate a virtual environment:
```sh
python -m venv venv
```

4. Install dependencies:

```sh
pip install -r requirements.txt
```

5. Set up the database:

Create a PostgreSQL database named blogdb.
Update the SQLALCHEMY_DATABASE_URI in config.py if necessary.

Initialize and apply migrations:

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

Running the Application
Start the Flask development server:

```sh
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

API Endpoints
GET /blogs: Get all blogs.
GET /blogs/<id>: Get a specific blog by ID.
POST /blogs: Create a new blog.
PUT /blogs/<id>: Update an existing blog by ID.
For detailed request and response formats, refer to the Postman collection (blog_api_collection.json) included in this repository.
