

# Setup Redis

You can run Redis locally using Docker Compose. In the repository root, run:

```bash
# Pull the Redis image and start the container in detached mode
docker compose up -d redis
```

This will expose Redis on port `6379` and create a persistent volume `redis_data`.

Make sure the Redis container is running before starting the backend. The backend connects to `localhost:6379` by default.

Once Redis is running, you can start the backend and frontend as before.

# Backend
cd .\backend
uvicorn main:app --reload

# Frontend
cd .\React
npm run dev