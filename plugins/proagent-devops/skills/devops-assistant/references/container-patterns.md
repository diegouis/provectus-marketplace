## Docker Containerization

### Optimized Multi-Stage Dockerfile

```dockerfile
# Build stage
FROM node:20-alpine AS builder
RUN apk add --no-cache python3 make g++
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --only=production && npm cache clean --force
COPY . .
RUN npm run build
RUN npm prune --production

# Runtime stage
FROM node:20-alpine AS runtime
RUN apk add --no-cache dumb-init curl && rm -rf /var/cache/apk/*
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./
ENV NODE_ENV=production PORT=3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1
USER nodejs
EXPOSE 3000
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/index.js"]
```

### Docker Compose Production Pattern

```yaml
version: '3.9'

x-healthcheck-defaults: &healthcheck-defaults
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 30s

services:
  api:
    build:
      context: ./api
      target: runtime
    restart: unless-stopped
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
      REDIS_URL: redis://redis:6379
    networks:
      - frontend
      - backend
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '2'
          memory: 1024M

  postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - backend
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD", "redis-cli", "ping"]

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    networks:
      - monitoring
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring
      - frontend
    ports:
      - "3000:3000"

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
  monitoring:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
```

## Production Docker Compose Patterns

Reference: `casdk-harness/docker-compose.prod.yml`

Additional production hardening beyond the standard Docker Compose pattern:

- Use `read_only: true` for container root filesystems where possible
- Mount only specific directories as writable via `tmpfs` mounts
- Set `no-new-privileges: true` in security options
- Use `cap_drop: [ALL]` and add back only required capabilities
- Configure log drivers with size rotation limits (`json-file` with `max-size` and `max-file`)
- Use Docker secrets instead of environment variables for sensitive values
