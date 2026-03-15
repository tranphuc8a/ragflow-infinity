---
sidebar_position: 2
slug: /deploy_guide/dev/environment_setup_windows
sidebar_custom_props: {
  categoryIcon: LucideLaptop
}
---
# Chuẩn bị môi trường dev trên Windows

Tài liệu này ưu tiên kịch bản **Windows + Docker Desktop + WSL2 + VS Code** vì đây là cách ít lỗi nhất để build/run/debug RAGFlow từ source.

---

## 1. Yêu cầu phần cứng và phần mềm

### Phần cứng tối thiểu

- CPU >= 4 cores
- RAM >= 16 GB
- Disk trống >= 50 GB

### Phần mềm nên có

- Windows 11 hoặc Windows 10 22H2+
- WSL2
- Ubuntu trên WSL2
- Docker Desktop
- VS Code
- Git
- Node.js >= `18.20.4`
- Python `3.12`
- `pipx`

## 2. Kiến nghị setup

Khuyến nghị mở repo bằng **VS Code Remote - WSL** và thao tác toàn bộ lệnh build/run trong Ubuntu WSL2.

Lý do:

- script của repo dùng `bash`
- worker có tối ưu Linux như `jemalloc`
- Docker Desktop tích hợp tốt với WSL2
- debug Python/Node trong VS Code ổn định hơn

## 3. Chuẩn bị WSL2

Nếu chưa có WSL2, cài từ PowerShell chạy quyền admin:

```powershell
wsl --install
```

Sau đó cài Ubuntu và kiểm tra:

```powershell
wsl -l -v
```

Đảm bảo distro Ubuntu của bạn đang ở version `2`.

## 4. Cấu hình `vm.max_map_count` cho Docker Desktop WSL2

Elasticsearch cần `vm.max_map_count >= 262144`.

### Cách tạm thời

Từ PowerShell:

```powershell
wsl -d docker-desktop -u root
sysctl -w vm.max_map_count=262144
```

### Cách giữ cố định

Tạo hoặc cập nhật file `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
kernelCommandLine = "sysctl.vm.max_map_count=262144"
```

Sau đó restart Docker Desktop hoặc chạy:

```powershell
wsl --shutdown
```

## 5. Clone repo và mở bằng VS Code

Trong Ubuntu WSL2:

```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow
```

Nếu bạn đang làm việc trên fork/branch nội bộ thì chỉ cần `cd` vào repo hiện có.

## 6. Cài Python toolchain

Trong WSL2:

```bash
python3.12 --version
pipx install uv pre-commit
```

Nếu máy chưa có Python 3.12, hãy cài trước rồi mới chạy `uv`.

## 7. Cài dependency backend

Theo hướng dẫn trong repo, dùng `uv` để đồng bộ môi trường:

```bash
uv sync --python 3.12 --all-extras
uv run download_deps.py
pre-commit install
```

Nếu bạn cần chạy test backend:

```bash
uv sync --python 3.12 --group test
uv pip install sdk/python --group test
```

## 8. Cài dependency frontend

```bash
cd web
npm install
cd ..
```

## 9. Kiểm tra các cổng local đang được repo dùng

Các cổng quan trọng mặc định:

- Frontend dev: `9222`
- Backend API: `9380`
- Admin API: `9381`
- Elasticsearch external port: `1200`
- MySQL external port: `5455`
- MinIO API: `9000`
- MinIO Console: `9001`
- Redis: `6379`

Nếu các cổng này bị chiếm, bạn cần đổi trong `docker/.env`, `conf/service_conf.yaml` hoặc frontend config tương ứng.

## 10. Lưu ý về `jemalloc`

Script chính thức của repo có dùng `jemalloc` cho `task_executor.py`.

Trên Ubuntu WSL2, cài thêm:

```bash
sudo apt update
sudo apt install -y libjemalloc-dev pkg-config
```

Tuy nhiên, để debug local, bạn **vẫn có thể chạy worker mà không cần `LD_PRELOAD`**. `jemalloc` là tối ưu thêm, không phải điều kiện bắt buộc để hiểu và debug luồng code.

## 11. Lưu ý về `HF_ENDPOINT`

Nếu môi trường của bạn truy cập Hugging Face chậm hoặc bị chặn, đặt mirror trước khi chạy backend:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

## 12. Kết quả mong đợi sau khi setup

Sau bước chuẩn bị, bạn cần có:

- `.venv/` đã được tạo
- dependency Python cài thành công
- dependency frontend cài thành công
- Docker Desktop chạy ổn
- WSL2 sẵn sàng để start base services và backend source

Bước kế tiếp là build/run full stack local.
