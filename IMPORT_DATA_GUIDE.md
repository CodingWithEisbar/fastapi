
# Hướng Dẫn Sử Dụng và Vận Hành Dự Án FastAPI

Đây là tài liệu ghi nhận các bước thiết lập, import dữ liệu và kiểm tra API cho dự án FastAPI này.

---

## 1. Cấu trúc thư mục

Dự án bao gồm các file chính sau:

- `main.py`: File chính của ứng dụng FastAPI, định nghĩa các API endpoint.
- `model.py`: Định nghĩa cấu trúc bảng (schema) trong cơ sở dữ liệu bằng SQLAlchemy.
- `schemas.py`: Định nghĩa schema (hình dạng dữ liệu) cho input và output của API bằng Pydantic.
- `crud.py`: Chứa các hàm xử lý các thao tác cơ sở dữ liệu (Create, Read, Update, Delete).
- `database.py`: Cấu hình kết nối đến cơ sở dữ liệu.
- `import_data.py`: Script để đọc dữ liệu từ file JSON và import vào database.
- `product.json`: File JSON chứa dữ liệu mẫu để import.

---

## 2. Thiết lập môi trường

Trước khi chạy ứng dụng, bạn cần kích hoạt môi trường ảo (virtual environment) và đảm bảo các thư viện cần thiết đã được cài đặt.

```bash
# Kích hoạt môi trường ảo
source .venv/bin/activate

# (Nếu cần) Cài đặt các thư viện từ file requirements.txt
# pip install -r requirements.txt 
```

---

## 3. Import Dữ Liệu Ban Đầu

Chúng ta sử dụng một script để đọc dữ liệu từ `product.json` và thêm vào cơ sở dữ liệu.

**Lưu ý:** Đảm bảo bạn đã kích hoạt môi trường ảo trước khi chạy lệnh này.

```bash
# Chạy script import_data.py
python import_data.py
```

Output mong đợi:

```
Đã đọc được 4 items từ file product.json.
Đã thêm: Sản phẩm A
Đã thêm: Sản phẩm B
Đã thêm: Sản phẩm C
Đã thêm: Sản phẩm D

Hoàn tất quá trình import dữ liệu!
Đã đóng kết nối database.
```

---

## 4. Chạy Ứng Dụng FastAPI

Sau khi import dữ liệu, bạn có thể khởi động server để bắt đầu nhận request.

```bash
# Chạy server FastAPI với Uvicorn
# Tùy chọn --reload sẽ tự động khởi động lại server khi có thay đổi trong code
uvicorn main:app --reload
```

Server sẽ chạy tại địa chỉ `http://127.0.0.1:8000`.

---

## 5. Kiểm Tra API với cURL

Sau khi server đã chạy, mở một cửa sổ terminal mới và sử dụng các lệnh `curl` sau để kiểm tra.

### Lấy danh sách tất cả các sản phẩm

Lệnh này sẽ gọi đến endpoint `GET /items/`.

```bash
curl -X GET "http://127.0.0.1:8000/items/"
```

### Thêm một sản phẩm mới

Lệnh này sẽ gọi đến endpoint `POST /items/` để tạo một item mới.

```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{
  "title": "Sản phẩm mới từ cURL",
  "description": "Đây là mô tả cho sản phẩm mới"
}'
```

### Lấy thông tin kết nối database

Lệnh này sẽ gọi đến endpoint `GET /database-name`.

```bash
curl -X GET "http://127.0.0.1:8000/database-name"
```

---

## Xử Lý Lỗi Thường Gặp

- **Lỗi `curl: (7) Failed to connect to 127.0.0.1 port 8000`:**
  - **Nguyên nhân:** Server FastAPI chưa được khởi động.
  - **Giải pháp:** Chạy lệnh `uvicorn main:app --reload` trong một terminal và đảm bảo nó đang hoạt động trước khi thực hiện lại lệnh `curl`.

