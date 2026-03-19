# Huong dan Dev Build va Run RAGFlow tu Source (Windows + Docker)

Tai lieu nay huong dan tung buoc de dev local:
- Service phu thuoc ben ngoai (DB, storage, queue, doc engine) chay bang Docker Compose.
- Backend Python, frontend web, va cac service Go chay tu source code.

## 1) Tong quan kien truc chay local

- Docker Compose (external deps):
  - MySQL
  - MinIO
  - Redis
  - Elasticsearch hoac Infinity (chon 1)
- Source code:
  - Backend Python API: `api/ragflow_server.py`
  - Task executor Python: `rag/svr/task_executor.py`
  - Frontend Vite: `web`
  - Go API/Admin service (tuy chon, hybrid mode): `cmd/server_main.go`, `cmd/admin_server.go`

## 2) Yeu cau moi truong

### 2.1 Phan mem can co

- Docker Desktop (Windows)
- Git
- Python 3.12 hoac 3.13
- Node.js >= 18.20.4
- npm
- pipx (khuyen nghi de cai uv)

### 2.2 Cong cu cho Python

```powershell
pipx install uv pre-commit
```

## 3) Lay source va cai dependencies cho source code

```powershell
git clone https://github.com/infiniflow/ragflow.git
cd ragflow

# Tao virtual env va cai dependencies Python
uv sync --python 3.13 --all-extras
uv run download_deps.py
pre-commit install
```

Ghi chu:
- `pyproject.toml` yeu cau Python trong khoang `>=3.12,<3.15`.
- Neu ban khong co 3.13, co the dung 3.12.

## 4) Dung cac service phu thuoc bang Docker Compose

Repo da co file compose gom cac dependency cho dev:
- `docker/docker-compose.dev-deps.yml`

### 4.1 Chay theo Elasticsearch (khuyen nghi mac dinh)

```powershell
docker compose -f docker/docker-compose.dev-deps.yml --profile elasticsearch up -d
```

### 4.2 Hoac chay theo Infinity

```powershell
docker compose -f docker/docker-compose.dev-deps.yml --profile infinity up -d
```

### 4.3 Kiem tra trang thai container

```powershell
docker compose -f docker/docker-compose.dev-deps.yml ps
```

Ban can thay cac container `healthy` (hoac `running` tuy service).

## 5) Cau hinh source backend cho local

File cau hinh local mac dinh:
- `conf/service_conf.yaml`

File nay trong repo da de san host local:
- MySQL: `localhost:5455`
- MinIO: `localhost:9000`
- Redis: `localhost:6379`
- Elasticsearch: `http://localhost:1200`
- Infinity: `localhost:23817`

### 5.1 Chon doc engine

- Neu chay profile `elasticsearch`:
  - Dat env `DOC_ENGINE=elasticsearch`
- Neu chay profile `infinity`:
  - Dat env `DOC_ENGINE=infinity`

## 6) Build va run backend Python tu source

Mo 2 terminal PowerShell trong thu muc goc repo.

### 6.1 Terminal 1: chay task executor

```powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = (Get-Location).Path
$env:DOC_ENGINE = "elasticsearch"   # doi thanh infinity neu can
$env:STORAGE_IMPL = "MINIO"

uv run python rag/svr/task_executor.py 0
```

### 6.2 Terminal 2: chay API server

```powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = (Get-Location).Path
$env:DOC_ENGINE = "elasticsearch"   # doi thanh infinity neu can
$env:STORAGE_IMPL = "MINIO"

uv run python api/ragflow_server.py
```

Ghi chu:
- Tren Linux/macOS ban co the dung script `docker/launch_backend_service.sh`.
- Tren Windows, cach chay truc tiep 2 process nhu tren de on dinh hon.

## 7) Build va run frontend tu source

Mo terminal PowerShell thu 3:

```powershell
cd web
npm install

# Frontend proxy ve backend Python (9380/9381)
$env:API_PROXY_SCHEME = "python"

npm run dev
```

Frontend mac dinh chay o:
- `http://127.0.0.1:9222`
- Admin UI: `http://127.0.0.1:9222/admin`

## 8) Kiem tra he thong da chay OK

Khi backend Python da len, test nhanh:

```powershell
curl http://127.0.0.1:9380/v1/system/ping
curl http://127.0.0.1:9380/v1/system/healthz
```

Ky vong:
- `ping` tra ve `pong`
- `healthz` tra ve JSON va ma 200 neu cac dependency thong.

## 9) (Tuy chon) Build va run Go services tu source (hybrid mode)

Phan Go hien tai can C++ static library va moi truong CGO, thuong de nhat khi chay tren WSL2/Linux.

### 9.1 Yeu cau them cho Go build

- Go 1.25+
- cmake
- g++
- libpcre2-dev

### 9.2 Build Go binaries

Trong WSL/Linux shell tai root repo:

```bash
./build.sh --all
```

Sinh ra:
- `bin/server_main`
- `bin/admin_server`

### 9.3 Run Go services

```bash
./bin/admin_server
./bin/server_main
```

Neu ban chay frontend theo hybrid mode, dat:

```powershell
$env:API_PROXY_SCHEME = "hybrid"
```

## 10) Stop he thong

### 10.1 Stop source processes

- Trong tung terminal dang chay source, bam `Ctrl + C`.

### 10.2 Stop external dependencies

```powershell
docker compose -f docker/docker-compose.dev-deps.yml down
```

Neu muon xoa ca volume du lieu local:

```powershell
docker compose -f docker/docker-compose.dev-deps.yml down -v
```

## 11) Troubleshooting nhanh

### 11.1 Frontend len nhung goi API loi

- Kiem tra backend Python dang chay o port `9380`.
- Kiem tra `API_PROXY_SCHEME=python` truoc khi `npm run dev`.

### 11.2 `healthz` bi 500

- Kiem tra compose profiles da dung (`elasticsearch` hoac `infinity`).
- Kiem tra bien `DOC_ENGINE` tren ca task executor va API server.
- Kiem tra port trong `conf/service_conf.yaml` co trung voi port expose cua compose.

### 11.3 Loi ket noi MySQL/MinIO/Redis

- Xem log container:

```powershell
docker compose -f docker/docker-compose.dev-deps.yml logs -f mysql
docker compose -f docker/docker-compose.dev-deps.yml logs -f minio
docker compose -f docker/docker-compose.dev-deps.yml logs -f redis
```
