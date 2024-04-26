from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse, HttpResponseBadRequest
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# LOGIN SIGN UP 
def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect("index")


def userin4(request):  
      if request.method=="POST":
         user=request.user
         name=request.POST.get('name')
         birthday=request.POST.get('birth')
         type_user=request.POST.get('type')
         phonenum=request.POST.get('phone')
         address=request.POST.get('adr')
         email=request.POST.get('email')
         try: 
            custom = Customer.objects.get(user=user)
            # Cập nhật thông tin cho khách hàng đã tồn tại
            custom.name = name
            custom.birthday = birthday
            custom.type_user = type_user
            custom.phonenum = phonenum
            custom.address = address
            custom.email = email
            custom.save()
            messages.success(request, mark_safe('Thay đổi thông tin người dùng thành công!'))
            return redirect('index')
         except Customer.DoesNotExist:
            custom = Customer.objects.create(user=user, name=name, birthday=birthday, type_user=type_user, phonenum=phonenum, address=address, email=email)
            custom.save()
            messages.success(request, mark_safe('Nhập thông tin người dùng thành công!'))
            return redirect('index')
      else:
          customer = request.user
          try:
              custom = Customer.objects.get(user=customer)
              name = custom.name
              birth = custom.birthday
              type = custom.type_user
              phone = custom.phonenum
              adr = custom.address
              email = custom.email
              return render(request, 'Manage/userin4.html', {'name': name, 'birth': birth, 'type': type, 'phone': phone, 'adr': adr, 'email': email,})
          except Customer.DoesNotExist:
              return render(request, 'Manage/userin4.html')
              

def Logout_page(request):
   logout(request)
   return redirect('index')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pw = request.POST.get('password')
        pw1 = request.POST.get('confirm_password')  # Sửa thành confirm_password
        if pw != pw1:
            messages.error(request, mark_safe('Mật khẩu nhập lại không khớp.'))
            return redirect('signup')
        try:
            user = User.objects.get(username=uname)
            messages.error(request, mark_safe('Tài khoản đã tồn tại.'))
            return redirect('logins')
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=email)
                messages.error(request, mark_safe('Email đã được sử dụng.'))
                return redirect('signup')
            except User.DoesNotExist:
                data = User.objects.create_user(uname, email=email, password=pw)  # Sử dụng password=pw để tránh lỗi khi tạo tài khoản
                data.save()
                messages.success(request, mark_safe('Tạo tài khoản thành công.'))
                return redirect('logins')
    else:
        return render(request, 'Manage/signup.html', {})
    
def logins(request):
   if request.method == 'POST'and request.POST:
      uname = request.POST.get('user')
      pw = request.POST.get('password')
      user = authenticate(request, username=uname, password=pw)
      if user is not None:
        login(request, user)
        return redirect('index')
      else:
         messages.error(request, mark_safe('Tài khoản hoặc mật khẩu không đúng.'))
   return render(request, 'Manage/login.html', {})

def password_reset(request):
   if request.method == 'POST':
      email = request.POST.get('email')
      try:
         user = User.objects.get(email=email)
         messages.success(request, mark_safe('Kiểm tra email của bạn để đặt lại mật khẩu.'))
      except User.DoesNotExist:
         messages.error(request, mark_safe('Email không tồn tại.'))
   return render(request, 'Manage/password_reset_conflirm.html', {})
# INDEX 

def index(request):
   return render(request, 'Manage/index.html')

def notify(request): 
   return render(request, 'Manage/notify.html')

# RESOURCE 
def search(request):
    searched_name = ""  # Default value for searched
    searched_adr = ""  # Default value for searched
    keys = []  # Default value for keys
    keys1 = []
    if request.method == "POST":
        searched_name = request.POST["searched_name"]
        searched_adr = request.POST["searched_adr"]
        keys = Product.objects.filter(name__contains = searched_name)
        keys1 = Product.objects.filter(adress__contains = searched_adr)
    return render(request, 'Manage/search.html', {"searched_name":searched_name , "searched_adr":searched_adr, "keys":keys, "keys1":keys1})

# MANAGE 
def manage(request):
    # Kiểm tra xem người dùng có đăng nhập hay không
    if request.user.is_authenticated:
        # Lấy user hiện tại
        current_user = request.user

        # Lấy các mùa vụ của người dùng hiện tại
        seasons = Season.objects.filter(user=current_user)

        # Lấy các đất đai của người dùng hiện tại dựa trên các mùa vụ
        lands = Land.objects.filter(season__in=seasons)

        # Lấy các cây trồng của người dùng hiện tại dựa trên các đất đai
        plants = Plant.objects.filter(land__in=lands)

        context = {
            'user': current_user,
            'season': seasons,
            'land': lands,
            'plant': plants,
        }
        return render(request, "Manage/manage.html", context)
    else:
        return render(request, "Manage/manage.html")

def get_season_info(request, season_id):
  """
  API endpoint to retrieve information for a specific season.
  """
  try:
    season = Season.objects.get(pk=season_id)
  except Season.DoesNotExist:
    return JsonResponse({'error': 'Season not found'}, status=404)

  data = {
    "season_name": season.season_name,
    "start_time": season.time_start,
    "end_time": season.time_end,
    "profit": season.profit,
  }

  return JsonResponse(data)

def get_land_info(request, land_id):

  try:
    land = Land.objects.get(pk=land_id)
  except Season.DoesNotExist:
    return JsonResponse({'error': 'Land not found'}, status=404)

  data = {
    "id": land.id,
      "name": land.land_name,
      "area": land.land_area,  
      "ph": land.land_pH,
      "moisture": land.land_doAm,  
      "position": land.land_pos
  }

  return JsonResponse(data)

def get_land_by_season(request, season_id):
  """
  Lấy danh sách mảnh đất theo mùa vụ.
  """

  # Lấy dữ liệu mảnh đất
  lands = Land.objects.filter(season=season_id)  # Access season using double underscore

  # Chuẩn bị dữ liệu JSON
  data = []
  for land in lands:
    data.append({
      "id": land.id,
      "name": land.land_name,
      "area": land.land_area,  # Add additional properties as needed
      "ph": land.land_pH,
      "moisture": land.land_doAm,  # Assuming doAm represents moisture
      "position": land.land_pos
    })

  return JsonResponse(data, safe=False)

def get_plant_by_land(request, land_id):
  """
  Lấy danh sách cây trồng theo mảnh đất.
  """

  # Lấy dữ liệu mảnh đất
  plants = Plant.objects.filter(land=land_id)
  

  # Chuẩn bị dữ liệu JSON
  data = []
  for plant in plants:
    data.append({
      "id": plant.id,
      "name": plant.plant_name,
      "timeDev": plant.plant_dev,  # Add additional properties as needed
      "type": plant.plant_type,
      "nd": plant.plant_ND,  # Assuming doAm represents moisture
      "bp": plant.plant_bp
    })

  return JsonResponse(data, safe=False)

def land_form(request):
    if request.method == 'POST':
        land_name = request.POST['land_name']
        land_pos = request.POST['land_pos']
        land_area = request.POST.get('land_area', 0)  # Default value if not provided
        land_pH = request.POST.get('land_pH', 7)  # Default value if not provided
        land_doAm = request.POST.get('land_doAm', 50.00)  # Default value if not provided
        selected_season_id = request.POST['id_mv']

        try:
            season = Season.objects.get(pk=selected_season_id)
        except Season.DoesNotExist:
            return HttpResponseBadRequest('Invalid season ID')

        land = Land.objects.create(
            land_name=land_name,
            land_pos=land_pos,
            land_area=land_area,
            land_pH=land_pH,
            land_doAm=land_doAm,
            season=season
        )

        messages.success(request, "Land created successfully!")
        return redirect("manage")  # Redirect to your desired page after success
    
    current_user = request.user
    user_seasons = Season.objects.filter(user=current_user)
    # Truyền danh sách vụ mùa vào context
    context = {'season_list': user_seasons}

    return render(request, "Manage/land_form.html", context)

def plant_form(request):
    if request.method == 'POST':
        plant_name = request.POST['plant_name']
        plant_dev = request.POST.get('plant_dev', 0)  # Default 0 months
        plant_type = request.POST['plant_type']  # Assuming ID for plant type
        plant_ND = request.POST.get('plant_ND', 0)
        plant_bp = request.POST.get('plant_bp', 0)
        selected_land_id = request.POST.get('land_id', None)
        try:
          land = Land.objects.get(pk=selected_land_id)
        except Land.DoesNotExist:
          return HttpResponseBadRequest('Invalid season ID')
       

        # Create new Plant object
        plant = Plant.objects.create(
            plant_name=plant_name,
            plant_dev=plant_dev,
            plant_type=plant_type,
            plant_ND=plant_ND,
            plant_bp=plant_bp, 
            land=land
        )

        messages.success(request, "Plant created successfully!")
        return redirect("manage")  # Redirect to success page (replace with your URL)

    # Lấy user hiện tại
    current_user = request.user

    # Lấy các mùa vụ của người dùng hiện tại
    seasons = Season.objects.filter(user=current_user)

    # Lấy các đất đai của người dùng hiện tại dựa trên các mùa vụ
    
   
    land_list = Land.objects.filter(season__in=seasons)
    context = {'land_list': land_list}

    return render(request, "Manage/plant_form.html", context)

def m_form(request):
    if request.method == 'POST':
        # Get form data and perform validation (improved)
        season_name = request.POST['name']
        time_start = request.POST['time_s']
        time_end = request.POST['time_e']
        profit = request.POST.get('num', 0)  # Get profit, default to 0

        # Validate data (example)
        if not season_name:
            messages.error(request, "Please enter a season name.")
            return render(request, "Manage/m_form.html")

        # Create and save Season
        season = Season.objects.create(
            season_name=season_name,
            time_start=time_start,
            time_end=time_end,
            profit=profit,
            user=request.user  # Assuming User model is linked
        )

        messages.success(request, "Season created successfully!")  # Success message
        return redirect("manage")  # Redirect to manage page

    else:
        return render(request, "Manage/m_form.html")

def infor(request):
    if request.method == 'GET':
        season_id = request.GET.get('id')



# MARKET 
def maker(request):
    if request.user.is_authenticated:
      key = Customer.objects.filter(user=request.user)
      if not key.exists():  # Check if the queryset is empty
        return render(request, 'Manage/maker.html')  
      else:
        customer = request.user.customer
        product = ""
        maker = ""
        keys1 = []
        keys2 = []
        keys1 = thitruong.objects.filter(ten_caytrong__contains=product)
        keys2 = thitruong.objects.filter(ten_thitruong__contains=maker)  
        if request.method == "POST":
            product = request.POST["product"]
            maker = request.POST["maker"]
            keys1 = thitruong.objects.filter(ten_caytrong__contains=product)
            keys2 = thitruong.objects.filter(ten_thitruong__contains=maker)
        context = {'product':product,'maker':maker,'keys1' : keys1, 'keys2': keys2, 'customer': customer}
        return render(request, 'Manage/maker.html', context)
    else:
        return render(request, 'Manage/maker.html')

def makerDetail(request): 
    return render(request, 'Manage/makerDetail.html')

def get_market_by_id(request, market_id):
    """
    Lấy thông tin thị trường dựa trên ID.
    """

    try:
        # Tìm thị trường dựa trên ID
        market = thitruong.objects.get(id_thitruong=market_id)

        # Chuẩn bị dữ liệu JSON
        data = {
            "id": market.id_thitruong,
            "caytrong_id": market.id_caytrong,
            "ten_caytrong": market.ten_caytrong,
            "ten_thitruong": market.ten_thitruong,
            "ten_nguoiban": market.ten_nguoiban,
            "gia": market.gia
        }

        return JsonResponse(data)
    except thitruong.DoesNotExist:
        return JsonResponse({"error": "Thị trường không tồn tại."}, status=404)

def maker_sell(request):
    customer = request.user.customer
    
    if request.method == 'POST':
        # Process form submission
        user = request.user
        ten_caytrong = request.POST.get('ten_caytrong')
        ten_thitruong = request.POST.get('ten_thitruong')
        gia = request.POST.get('gia')
        mota = request.POST.get('mota')    

        # Create a new record in thitruong_ban table
        thitruong_ban_obj = thitruong_ban.objects.create(
            ten_caytrong=ten_caytrong,
            ten_thitruong=ten_thitruong,
            gia=gia,
            mota=mota,
            user=user
        )

        # Add a success message
        messages.success(request, "Nhập sản phẩm thành công")
        # Redirect to the same view to prevent form resubmission
        return redirect('maker_sell')

    else:
        # Fetch existing data
        username = request.user
        list_maker = thitruong_ban.objects.filter(user=username)
        context = {'list_maker': list_maker, 'customer': customer}
        return render(request, 'Manage/maker_sell.html', context)

# CONTACT 
def contact(request):
        if request.method == 'POST':  # Kiểm tra xem request là phương thức POST hay không
            # Lấy dữ liệu người dùng nhập từ form
            user = request.user
            hoten = request.POST.get('hoten')
            email = request.POST.get('email')
            loinhan = request.POST.get('loinhan')
            # Tạo một bản ghi mới trong bảng Contact
            lienhe = Contact.objects.create(user=user, hoten=hoten, email=email, loinhan=loinhan)
            lienhe.save()
            # Lưu lại thông báo thành công
            messages.success(request, "Gửi phản hồi thành công")
        return render(request, 'Manage/contact.html', {})
    

def aboutus(request):
            return render(request, 'Manage/aboutus.html')

# SUBSCRIBE 
def send_subscription_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        send_mail(
            'Chào mừng bạn đến với FOF',
            'Bạn đã đăng ký nhận tin thành công.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return redirect('index')

    