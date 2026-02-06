# StoreManager Gate

A FastAPI service for managing user permissions with DynamoDB backend.

## Prerequisites

- Python 3.10+
- Docker (for local DynamoDB)

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example environment file and update values:

```bash
cp .env.example .env
```

| Variable                | Description       | Default                 |
| ----------------------- | ----------------- | ----------------------- |
| `AWS_ACCESS_KEY_ID`     | AWS access key    | `local`                 |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key    | `local`                 |
| `AWS_DEFAULT_REGION`    | AWS region        | `us-east-1`             |
| `DYNAMODB_ENDPOINT_URL` | DynamoDB endpoint | `http://localhost:8000` |

### 4. Start local DynamoDB

```bash
docker-compose up -d
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

Or use FastAPI's development server:

```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Create User

```http
POST /user
Content-Type: application/json

{
  "username": "john",
  "permissions": ["read", "write"]
}
```

**Response (200):**

```json
{
  "username": "john",
  "permissions": ["read", "write"]
}
```

**Error (409):** User already exists

---

### Get User Permissions

```http
GET /user/permissions?username=john
```

**Response (200):**

```json
{
  "username": "john",
  "permissions": ["read", "write"]
}
```

---

### Update User Permissions

```http
PUT /user/permissions
Content-Type: application/json

{
  "username": "john",
  "permissions": ["read", "write", "delete"]
}
```

**Response (200):**

```json
{
  "username": "john",
  "permissions": ["read", "write", "delete"]
}
```

**Error (404):** User not found

---

## Project Structure

```
├── main.py                    # FastAPI application & routes
├── config.py                  # Configuration settings
├── database.py                # DynamoDB connection
├── permissions_repository.py  # Data access layer
├── schemas.py                 # Pydantic models
├── exceptions.py              # Custom exceptions
├── docker-compose.yml         # Local DynamoDB setup
├── requirements.txt           # Python dependencies
└── .vscode/
    └── launch.json            # VS Code debug configuration
```

### API Documentation

Once running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
