# **TÊN ĐỀ TÀI: QUẢN LÝ NÔNG SẢN**

__Nội dung__: Hướng đến đối tượng thương lái, nông dân và người tiêu dùng
có nhu cầu tìm kiếm nguồn nông sản sạch với giá rẻ. Bên cạnh đó trang
web cũng là công cụ để quản lý mùa vụ cho nông dân.
## **HƯỚNG DẪN SỬ DỤNG WEBSITE**
- Link website: https://www.foft4k.me
- Docker: docker pull dark1234tan735/fof-app
- Link hướng dẫn: https://drive.google.com/file/d/1GBuCpVVOr2j1Wqhj0KYKuELuc766_6tQ/view?usp=sharing
## **PHÂN CÔNG CÔNG VIỆC THÀNH VIÊN**
- Xem chi tiết tại sheet: https://docs.google.com/spreadsheets/d/1OX2Wu_FgxVtVBel5lGmshl33nZuvg2LNXuAl5wX8C_Y/edit?usp=sharing

## **THÀNH VIÊN:**
 
|Họ và tên|MSSV|Chức vụ|
| :------------:|:-------------:|:-----:|
|Nguyễn Đức Tấn|22521303|nhóm trưởng|
|Lâm Xuân Thái|22521317|thành viên|
|Phạm Minh Tân|22521310|thành viên|
|Phan Nguyễn Nhật Trâm|22521501|thành viên|
|Nguyễn Kim Khánh|22520643|thành viên|

## **HƯỚNG DẪN SETUP MÔI TRƯỜNG DJANGO**

### **Cài đặt Python và VS Code**
- Cài đặt Python (https://www.python.org/downloads/)
- Cài đặt VS Code (https://code.visualstudio.com/download)

### **Cài đặt các extension cần thiết cho VS Code**
- Mở VS Code và cài đặt các extension sau để hỗ trợ phát triển Django:
  - Python
  - Django

### **Chạy website với VS Code**
- Mở VS Code và mở thư mục chứa dự án
- Mở terminal trong VS Code bằng cách chọn Terminal -> New Terminal
- Cài đặt Django bằng lệnh: pip install django
- Cài thêm:
  - pip install django-allauth
  - pip install social-auth-app-django
- Khởi động máy chủ phát triển bằng lệnh: python manage.py runserver

## **TRIỂN KHAI WEB BẰNG DOCKER**
- Cài đặt docker : https://www.docker.com/products/docker-desktop/ 
- Mở terminal và dán link: docker pull dark1234tan735/fof-app
- Sau khi hoàn tất vào docker desktop click biểu tượng ▶️
- Đặt ports = 500 -> Run
- Vào trình duyệt nhập địa chỉ: 127.0.0.1:500


## **TÍNH NĂNG**

### **Cơ bản**
- Đăng ký, đăng nhập (bằng username, bằng tài khoản Google) 
- Nhập thông tin người dùng
- Quản lý việc trồng trọt của nông dân
  - Nhập các thông tin về mùa vụ như: tên, thời gian bắt đầu, kết thúc, năng suất đặt ra (thêm, xoá, sửa)  
  - Nhập các thông tin về đất đai được sử dụng trong mùa vụ đó (tên đất, vị trí, diện tích, độ pH, độ ẩm) – các thao tác thêm, xoá, sửa 
  - Nhập các thông tin về cây trồng (chọn cây trồng, thời gian phát triển, loại cây, chất khoáng cần thiết, chu kỳ bón phân) – thêm, xoá, sửa 
  - Hiển thị bản đồ trực quan về mảnh đất của người dân 
  - Đánh giá tình trạng đất đai dựa trên độ ẩm và độ pH
  - Tính toán số ngày cây trồng chuẩn bị thu hoạch
- Tìm kiếm thị trường đến bán nông sản hoặc thu mua
  - Mode 1: dành cho nông dân
    - Tìm kiếm thị trường để bán nông sản dựa trên các thông tin về nông sản muốn bán và nơi muốn bán
    - Xác nhận thông tin
    - Gửi thông báo đến thương lái 
  - Mode 2: dành cho thương lái 
    - Nhập các nhu cầu của thương lái
    - Tìm kiếm nông dân muốn bán
- Tìm kiếm nguồn nguyên vật liệu giá rẻ cho nông nghiệp 
- Liên hệ (nhận feedback từ người dùng)

### **Nâng cao**
- Auto complete 
- AJAX (tại trang tìm kiếm thị trường)

## **SỰ KHÁC BIỆT**
- Phiên bản Final đã sửa lại các lỗi được giảng viên feedback như:  
  - Lỗi responsive
  - Người dùng được phép chọn cây trồng thay vì nhập 
  - Sửa lỗi tràn auto complete
  - Thêm chức năng sắp xếp theo giá tiền ở trang tìm kiếm thị trường 
  - Chỉnh sửa chức năng hiển thị bản đồ, đánh giá tình trạng cây trồng. 
  - Sửa thanh navbar
  - Chỉnh sửa chat AI

## **OTHER**
- Web khi deloy có sử dụng giao thức HTTPS, chứng chỉ SSL/TLS 
- Dùng CloudFlare chống DDos, Botnet  


## **CÔNG NGHỆ SỬ DỤNG**
- __FRONT END__: HTML, CSS (Bootstrap), JS 
- __BACK END__: Django
- __DATABASE__: SQLite 
