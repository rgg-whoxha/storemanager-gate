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
| `AWS_ACCESS_KEY_ID`     | AWS access key    | -                       |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key    | -                       |
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

The API will be available at `http://localhost:8000`.

## API Endpoints

### Get User Permissions

```http
POST /user/permissions
Content-Type: application/json

{
  "username": "user@example.com"
}
```

**Response:**

```json
{
  "user": "user@example.com",
  "permissions": [...]
}
```

## Project Structure

```
├── main.py                    # FastAPI application entry point
├── config.py                  # Configuration settings
├── database.py                # DynamoDB connection
├── permissions_repository.py  # Data access layer
├── schemas.py                 # Pydantic models
├── docker-compose.yml         # Local DynamoDB setup
└── requirements.txt           # Python dependencies
```

## Development

### API Documentation

Once running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
