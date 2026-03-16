
import json
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine
import model

# Đảm bảo bảng đã được tạo
model.Base.metadata.create_all(bind=engine)

def import_from_json(db: Session, file_path: str):
    """
    Hàm đọc dữ liệu từ file JSON và thêm vào cơ sở dữ liệu.
    """
    try:
        # Mở và đọc file JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            items_data = json.load(f)
        
        print(f"Đã đọc được {len(items_data)} items từ file {file_path}.")

        # Lặp qua từng item trong file JSON
        for item_data in items_data:
            # Bỏ qua trường 'id' từ file JSON vì database sẽ tự tạo
            item_to_create = schemas.ItemCreate(
                title=item_data.get("title"),
                description=item_data.get("description")
            )
            # Sử dụng hàm crud để tạo item mới
            crud.create_item(db=db, item=item_to_create)
            print(f"Đã thêm: {item_to_create.title}")

        print("\nHoàn tất quá trình import dữ liệu!")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn: {file_path}")
    except json.JSONDecodeError:
        print(f"Lỗi: File JSON không hợp lệ: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")


if __name__ == "__main__":
    # Lấy một session từ database
    db = SessionLocal()
    try:
        # Đường dẫn tới file JSON của bạn
        # User mentioned the file is in `input_data/product.json`
        # I'll create that file first.
        json_file_path = "/home/user/fastapi/input_data/product.json" 
        import_from_json(db, json_file_path)
    finally:
        # Luôn đóng session sau khi hoàn tất
        db.close()
        print("Đã đóng kết nối database.")

