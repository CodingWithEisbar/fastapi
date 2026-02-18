from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="postgresql://admin:Nguyen@123@194.233.93.255:22641/DB_POOL"


# Create an engine to stay connect to database
engine = create_engine(
    DATABASE_URL,
    pool_size=5,          # Giữ sẵn 5 kết nối trong Pool
    max_overflow=10,      # Cho phép mở thêm tối đa 10 kết nối nữa nếu lúc cao điểm (tổng = 15)
    pool_timeout=30,      # Nếu Pool cạn kiệt, chờ tối đa 30s để lấy kết nối, quá thời gian sẽ báo lỗi
    pool_recycle=1800     # Tự động hủy và tạo lại kết nối sau mỗi 30 phút (tránh lỗi database tự ngắt kết nối cũ)
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine
)

Base
