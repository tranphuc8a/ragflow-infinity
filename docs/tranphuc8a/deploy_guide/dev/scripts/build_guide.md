# Build guide cho dev moi (Ubuntu) - RAGFlow

Tai lieu nay tong hop cach build, run, debug va theo doi RAGFlow tu source code moi nhat, theo huong:
- FE + BE chay tu source.
- Cac service phu thuoc (MySQL, MinIO, Redis, doc engine) chay bang Docker Compose.

Muc tieu la dev moi co the:
1. Setup may Ubuntu moi (chua co env).
2. Build + run thanh cong lan dau.
3. Tu lan sau chi can chay 1 script de len toan bo stack.

## 1) Kien truc local dev

- Source code:
  - Backend API Python: `api/ragflow_server.py` (port 9380)
  - Admin API Python: cung process backend, endpoint admin qua 9381 theo proxy
  - Task executor Python: `rag/svr/task_executor.py`
  - Frontend Vite: `web` (mac dinh port 9222)
- Docker Compose dependency:
  - MySQL (port host 5455)
  - MinIO (9000/9001)
  - Redis (6379)
  - Elasticsearch (1200) hoac Infinity (23817/23820)

Thong so tren khop voi:
- `conf/service_conf.yaml`
- `docker/.env`
- `docker/docker-compose.dev-deps.yml`
- `web/vite.config.ts`

## 2) Yeu cau toi thieu

- Ubuntu 22.04+ (khuyen nghi 24.04)
- CPU >= 4 core
- RAM >= 16 GB
- Disk trong >= 50 GB
- Quyen sudo
- Internet de pull image Docker + dependency

## 3) Buoc 0 - Chuan bi he dieu hanh tu trang thai trong

Chay tat ca lenh sau tren terminal Ubuntu:

```bash
sudo apt update
sudo apt install -y \
  ca-certificates curl gnupg lsb-release software-properties-common \
  git jq unzip build-essential pkg-config \
  python3 python3-venv python3-pip pipx \
  libjemalloc-dev

pipx ensurepath
```

Mo terminal moi sau `pipx ensurepath` de nhan duong dan pipx.

## 4) Cai Docker Engine + Docker Compose plugin

Neu may chua co Docker:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
```

Dang xuat/dang nhap lai hoac reboot de ap dung group `docker`.

Kiem tra:

```bash
docker --version
docker compose version
```

## 5) Buoc 1 - Lay source va cai tool dev

```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow

pipx install uv pre-commit
```

## 6) Buoc 2 - Build + run lan dau (mot lan duy nhat)

Repo nay da co script bootstrap cho Ubuntu:
- `scripts/dev_bootstrap_ubuntu.sh`

Script nay se:
- Cai dependency Python vao `.venv` bang `uv sync --python 3.12 --all-extras`
- Tai them model/deps can thiet bang `uv run download_deps.py`
- Cai frontend dependency (`npm install` trong `web/`)
- Cai git hook (`pre-commit install`)

Chay:

```bash
chmod +x scripts/dev_bootstrap_ubuntu.sh scripts/dev_up.sh scripts/dev_down.sh
./scripts/dev_bootstrap_ubuntu.sh
```

Neu ban dung NodeJS moi cai va chua co, script se bao huong dan cai nhanh bang nvm.

Neu gap loi mirror Python (403/timeout), co the chay voi index ro rang:

```bash
PYPI_INDEX_URL=https://pypi.org/simple ./scripts/dev_bootstrap_ubuntu.sh
```

Hoac neu mang noi bo chi cho phep mirror khac:

```bash
PYPI_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple ./scripts/dev_bootstrap_ubuntu.sh
```

Neu gap loi resolver cua uv cho environment khong phai may hien tai (vi du split aarch64), co the ep marker theo may dang dung:

```bash
UV_ENVIRONMENTS="sys_platform == 'linux' and platform_machine == 'x86_64'" ./scripts/dev_bootstrap_ubuntu.sh
```

## 7) Buoc 3 - Run he thong (dependency docker + FE + BE source)

Chay 1 lenh:

```bash
./scripts/dev_up.sh
```

Mac dinh:
- Doc engine: `elasticsearch`
- Proxy FE -> BE: `python`

URL mac dinh:
- FE: http://127.0.0.1:9222
- BE ping: http://127.0.0.1:9380/v1/system/ping
- BE healthz: http://127.0.0.1:9380/v1/system/healthz

### Doi qua Infinity

```bash
DOC_ENGINE=infinity ./scripts/dev_up.sh
```

## 8) Tu lan sau: chi can 1 script

Sau khi lan dau da thanh cong, moi lan bat dau lam viec chi can:

```bash
./scripts/dev_up.sh
```

Script se tu dong:
- Up dependency compose profile phu hop.
- Start task executor + backend Python (neu chua chay).
- Start frontend dev server (neu chua chay).
- Ghi log vao `.dev/logs/`.

## 9) Stop dich vu

Dung source process (giu dependency docker de lan sau khoi dong nhanh):

```bash
./scripts/dev_down.sh
```

Dung ca dependency docker:

```bash
./scripts/dev_down.sh --with-deps
```

## 10) Debug va theo doi ung dung

### Xem log runtime

```bash
tail -f .dev/logs/task_executor.log
tail -f .dev/logs/ragflow_server.log
tail -f .dev/logs/frontend.log
```

### Xem log dependency docker

```bash
docker compose -f docker/docker-compose.dev-deps.yml logs -f mysql minio redis es01 infinity
```

### Bat debugpy cho backend

Neu can attach debugger tu IDE vao backend Python:

```bash
RAGFLOW_DEBUGPY_LISTEN=5678 ./scripts/dev_up.sh
```

Sau do attach debugger vao `127.0.0.1:5678`.

## 11) Checklist xac nhan sau khi run

- `curl http://127.0.0.1:9380/v1/system/ping` tra ve `pong`
- `curl http://127.0.0.1:9380/v1/system/healthz` tra ve HTTP 200
- Mo FE thanh cong tai http://127.0.0.1:9222
- Dang nhap/tao account local duoc

## 12) Loi thuong gap va cach xu ly nhanh

### 12.1 `docker: permission denied`

Ban chua nhan group `docker`:
- Kiem tra `groups | grep docker`
- Dang xuat dang nhap lai, hoac `newgrp docker`

### 12.2 FE khong goi duoc API

- Kiem tra backend log: `.dev/logs/ragflow_server.log`
- Kiem tra backend da len port 9380
- Kiem tra env `API_PROXY_SCHEME` (mac dinh la `python`)

### 12.3 healthz tra 500

- Kiem tra dependency co len het khong:
  - `docker compose -f docker/docker-compose.dev-deps.yml ps`
- Kiem tra profile dung voi `DOC_ENGINE`.

### 12.4 Loi khi cai Python deps

- Thu cap nhat uv:
  - `pipx upgrade uv`
- Thu chay lai:
  - `uv sync --python 3.12 --all-extras`

---

Neu can chay theo che do hybrid/go, co the mo rong them script rieng. Trong huong dan nay uu tien luong Python thuong dung nhat cho dev moi.
