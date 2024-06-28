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
## **TRẢ LỜI CÂU HỎI SEMINAR**
# Django FAQs

## Câu 1: Các hàm xử lý sẽ nằm ở đâu trong Django?

**Trả lời:**
Trong Django, các hàm xử lý (view functions) thường được đặt trong file `views.py` của mỗi ứng dụng (app) trong dự án. Cụ thể, trong file `views.py`, bạn sẽ định nghĩa các view functions, mỗi view function sẽ xử lý một request cụ thể và trả về một response tương ứng.

Ví dụ, một view function đơn giản có thể như sau:

```python
# views.py
from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello, Django!'
    }
    return render(request, 'index.html', context)
```

## Câu 2: Cách tối ưu hoá hiệu suất của ứng dụng Django, các chiến lược và công cụ nào có thể được dùng?
**Trả lời:** 
Để tối ưu hóa hiệu suất của ứng dụng Django, có nhiều chiến lược và công cụ có thể được sử dụng, bao gồm: Thay RESR API mặc định bằng 1 API khác
1. **Caching:**
2. **Tối ưu hóa cơ sở dữ liệu:**
    - Sử dụng các chỉ mục (indexes) để tăng tốc độ truy vấn.
    - Tối ưu hóa các truy vấn SQL, sử dụng ORM một cách hiệu quả.
    - Phân trang dữ liệu thay vì trả về toàn bộ.
3.  **Tối ưu hóa assets (CSS, JavaScript, hình ảnh):**
    - Sử dụng các công cụ nén, minify code.
    - Sử dụng Content Delivery Network (CDN) để phân phối các tài nguyên tĩnh.
    - Lazy loading để tải các tài nguyên chỉ khi cần thiết. (AJAX)
4.  **Tối ưu hóa Django ORM:**
    - Sử dụng các phương thức select_related() và prefetch_related() để giảm số lượng truy vấn.
    - Sử dụng các annotation và aggregation để tránh truy vấn dư thừa.
5.  **Sử dụng các công cụ profiling:**
    - Django Debug Toolbar để phân tích các truy vấn, template, middleware.
    - Yappi, cProfile để phân tích hiệu suất mã Python.
6.  **Scaling ứng dụng:**
    - Sử dụng load balancer để phân tán lưu lượng.
    - Sử dụng các công nghệ như Celery, RabbitMQ để xử lý các tác vụ nền.
    - Sử dụng các dịch vụ caching phân tán như Memcached, Redis.
## Câu 3: Giải thích về template và các thao tác nâng cao?
**Trả lời:** 
Trong Django, template là một cách để tách biệt logic xử lý (trong views) với giao diện người dùng (HTML). Các template cho phép bạn tạo ra các trang web động bằng cách kết hợp dữ liệu từ views với các thẻ HTML.
Một số thao tác nâng cao với template trong Django bao gồm:
1.  **Template inheritance:**
    - Cho phép tạo ra một "base" template chứa các phần chung, như header, footer, và các template con kế thừa từ "base" template này.
    - Giúp tránh lặp lại code và dễ dàng thay đổi giao diện toàn ứng dụng.
    - Ví dụ: trong 1 dự án Django, các phần như header, footer bạn chỉ cần code trong base và sau đó tái sử dụng lại.
2.  **Template tags và filters:**
    - Template tags cho phép thực hiện các logic lập trình cơ bản như vòng lặp, điều kiện, v.v. trong template.
    - Template filters cho phép format, chuyển đổi dữ liệu trước khi hiển thị.
    - Ví dụ: `{% if condition %}, {% for item in list %}`
3.  **Template context processors:**
    - Là các hàm Python trả về một dict chứa các biến sẽ được thêm vào context của mọi template.
    - Giúp chia sẻ dữ liệu phổ biến giữa các template.
4.  **Template rendering:**
    - Sử dụng hàm render() trong views để trả về một template được render với dữ liệu context.
    - Ví dụ: `return render(request, 'my_template.html', {'key': value})`
5.  **Template loaders:**
    - Cho phép tùy chỉnh cách Django tìm kiếm và load các template.
    - Ví dụ: load template từ database thay vì file hệ thống.
6.  **Template caching:**
## Câu 4: Django bảo mật như nào mà bạn liên hệ mạnh mẽ, phân quyền Django như nào là tối ưu nhất?
**Trả lời:** 
### Django có nhiều tính năng bảo mật mạnh mẽ nhằm bảo vệ ứng dụng web khỏi các cuộc tấn công phổ biến. Một số tính năng bảo mật chính của Django bao gồm:
1.  **Cross-Site Scripting (XSS) Protection:**
    -   Django tự động làm sạch dữ liệu đầu vào trước khi hiển thị, ngăn chặn các script độc hại.
    -   Sử dụng các template tags và filters để an toàn hóa dữ liệu.
2.  **Cross-Site Request Forgery (CSRF) Protection:**
    -   Django tích hợp sẵn cơ chế CSRF protection, chặn các yêu cầu giả mạo từ các trang web khác.
    -   Sử dụng token CSRF trong form để xác thực yêu cầu.
        Lưu ý: cần đảm bảo rằng CSRF middleware trong Django được cấu hình để tin tưởng các yêu cầu proxy. Bạn có thể cần cấu hình danh sách trắng (whitelist) cho các header hoặc tùy chọn nào đó để bỏ qua CSRF protection đối với các yêu cầu từ proxy.

3.  **SQL Injection Protection:**
    -   Django sử dụng ORM (Object-Relational Mapping) để tạo truy vấn SQL, tránh được các lỗ hổng SQL Injection.
    -   Sử dụng các tham số đánh dấu trong các truy vấn thay vì nối chuỗi.
4.  **Secure Sessions:**
    -   Django mã hóa và ký session data để tránh các cuộc tấn công session hijacking.
    -   Cung cấp các tùy chọn bảo mật session như HttpOnly, Secure cookies.
5.  **Secure Password Hashing:**
    -   Django sử dụng các thuật toán băm mạnh mẽ như Argon2, Bcrypt để lưu trữ mật khẩu.
    -   Tự động áp dụng các thuật toán băm mới khi cần thiết.
### Về phân quyền, Django cung cấp hệ thống quản lý người dùng và quyền mạnh mẽ:
1.  **User Model:**
    -   Django có một user model mặc định, nhưng bạn cũng có thể tùy chỉnh model này.
    -   Các trường như username, email, password, groups, permissions.
2.  **Permissions:**
    -   Django có các loại permissions cơ bản như add, change, delete, view.
    -   Bạn có thể tạo các permission tùy chỉnh cho từng model.
3.  **Groups:**
    -   Nhóm người dùng với các quyền được gán sẵn.
    -   Thuận tiện khi quản lý quyền truy cập cho nhiều người dùng.
4.  **Authentication Backends:**
    -   Django hỗ trợ nhiều loại authentication backends như ModelBackend, RemoteUserBackend.
    -   Cho phép tích hợp với các hệ thống authentication bên ngoài.

## Câu 5: Để tối ưu hiệu suất của các truy vấn trong Django DRM thì nên làm gì? 
**Trả lời:** 
Để tối ưu hiệu suất của các truy vấn trong Django ORM, bạn có thể thực hiện các bước sau:
1.  **Sử dụng Queryset API hiệu quả:**
    -   Sử dụng các phương thức Queryset như `filter()`, `exclude()`, `order_by()` để thu hẹp kết quả trước khi truy vấn.
    -   Tránh sử dụng `all()` khi không cần thiết, vì nó trả về toàn bộ bản ghi.
2.  **Sử dụng Prefetch/Select_related:**
    -   Sử dụng `prefetch_related()` để tải các relationship fields cùng lúc.
    -   Sử dụng `select_related()` để tải các foreign key fields cùng lúc.
    -   Giúp tránh các truy vấn N+1.
3.  **Caching:**
    -   Sử dụng Django cache framework để lưu trữ kết quả truy vấn.
    -   Áp dụng caching ở các vị trí thích hợp, như trang chủ, trang chi tiết, v.v.
4.  **Lazy Loading:**
    -   Chỉ tải dữ liệu khi thực sự cần thiết, thay vì tải toàn bộ ngay từ đầu.
    -   Sử dụng các phương thức như iterator(), values(), values_list().
5.  **Sử dụng Indexing:**
    -   Tạo index cho các trường được sử dụng thường xuyên trong các truy vấn.
    -   Giúp tăng tốc độ truy vấn.
6.  **Tối ưu hóa câu truy vấn:**
    -   Sử dụng các hàm aggregation như annotate(), count(), sum() thay vì thực hiện trong Python.
    -   Tối ưu các câu truy vấn phức tạp bằng cách chia nhỏ.
7.  **Sử dụng Raw SQL:**
    -   Trong trường hợp cần thực hiện các truy vấn phức tạp, có thể sử dụng Raw SQL.
    -   Giúp tối ưu hóa hiệu suất, nhưng cần chú ý đến vấn đề bảo mật.
8.  **Theo dõi và phân tích hiệu suất:**
    -   Sử dụng các công cụ như django-silk, django-debug-toolbar để theo dõi và phân tích hiệu suất.
    -   Từ đó, bạn có thể xác định được những chỗ cần tối ưu hóa.


