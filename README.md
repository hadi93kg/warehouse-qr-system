نسخه‌ی انگلیسی — English README

# Warehouse QR Inventory System  
A complete FastAPI-based warehouse inventory system with automatic QR code generation and product detail display upon scanning.

## 🚀 Features
- Add products with name, description and price  
- Auto-generate QR codes for each product  
- Scan QR to view product details  
- Dashboard for managing inventory  
- SQLite database with persistent storage  
- Clean and mobile-friendly UI  

## 🛠 Technologies Used
- FastAPI
- Jinja Templates
- SQLAlchemy
- SQLite
- Python QRCode
- HTML/CSS

## 📸 How It Works
1. Add a new product  
2. System generates a QR code automatically  
3. Scan QR to open product detail page  
4. Manage products in the dashboard  

## ⚠️ Important Note about Render Free Hosting
The live demo is hosted on Render Free Tier.  
This service shuts down the server after a few minutes of inactivity, which resets the SQLite database.

On a real VPS or paid hosting, data will remain persistent and will not be deleted.

## 🚀 Possible Future Enhancements
This project has a scalable structure and can be easily upgraded to a professional version.  
Some upgrade possibilities include:

- User authentication & admin panel
- Product categories
- Stock In/Out system
- Advanced analytics and charts
- Migration to PostgreSQL for permanent data
- Product image upload
- Mobile-friendly API endpoints
- PWA (offline-ready)
- User role management (Admin / Staff)

The current version is a simple demo suitable for portfolio and testing, and can be upgraded to an enterprise-grade warehouse system.


## 📦 Installation & Run
`bash
pip install -r requirements.txt
uvicorn app.main:app --reload

Access the app:

http://127.0.0.1:8000

🌐 LIVE DEMO (RENDER)

(https://warehouse-qr-system.onrender.com/)


__________________________


# سیستم انبارداری و مدیریت کالا با QR Code  
یک پروژه‌ی کامل برای مدیریت کالاها در انبار، تولید QR Code برای هر محصول، ثبت موجودی و مشاهده‌ی اطلاعات محصول با اسکن QR.

## 🚀 ویژگی‌های اصلی پروژه
- افزودن محصول جدید همراه با نام، توضیحات و قیمت  
- تولید خودکار QR Code برای هر محصول  
- مشاهده‌ی جزئیات کالا با اسکن QR Code  
- نمایش داشبورد محصولات  
- ذخیره‌سازی دیتای پایدار با SQLite  
- رابط کاربری ساده و شکیل  
- سازگار با گوشی (Mobile-Friendly)

## 🛠 تکنولوژی‌ها و ابزارهای استفاده شده
- FastAPI
- Jinja2 Templates
- SQLAlchemy
- SQLite
- Python QRCode
- HTML/CSS
- ⚡ قابل استقرار در Render ،Vercel ،Railway و ...

## 📸 نحوه‌ی عملکرد سیستم
1. محصول جدید را اضافه می‌کنید  
2. سیستم به‌صورت خودکار QR Code تولید و ذخیره می‌کند  
3. با اسکن QR Code وارد صفحه‌ی جزئیات محصول می‌شوید  
4. از داشبورد می‌توانید همه محصولات را مشاهده کنید  

## ⚠️ نکته مهم درباره نسخه آنلاین (Render Free)
نسخه‌ی فعلی که روی Render میزبانی شده است، به دلیل محدودیت‌های نسخه رایگان این سرویس، پس از چند دقیقه عدم فعالیت، سرور ریست می‌شود.  
در نتیجه داده‌ها (محصولات ثبت‌شده) ممکن است پاک شوند.

در سرور واقعی (VPS یا هاست دائمی) این مشکل وجود ندارد و داده‌ها به صورت کامل ذخیره و پایدار خواهند بود.

## 🚀 قابلیت‌های قابل ارتقا در نسخه حرفه‌ای
این پروژه ساختاری استاندارد دارد و به‌راحتی می‌تواند ارتقا یابد.  
چند ویژگی که می‌توان به نسخه حرفه‌ای اضافه کرد:

- سیستم ورود و پنل مدیریت کاربران (Authentication)
- اضافه کردن دسته‌بندی کالاها (Categories)
- ثبت ورود/خروج کالا (Stock In/Out)
- گزارش‌گیری پیشرفته و نمودارها
- اتصال به دیتابیس حرفه‌ای PostgreSQL
- آپلود عکس محصول
- اضافه کردن API موبایل
- نسخه PWA برای استفاده آفلاین
- سطح دسترسی کاربران (Roles)

در حال حاضر این پروژه به عنوان نسخه‌ی ساده و تستی برای رزومه و نمونه‌کار ارائه شده است و قابلیت ارتقا به نسخه سازمانی را دارد.



## 📦 نصب و راه‌اندازی
`bash
pip install -r requirements.txt
uvicorn app.main:app --reload

سپس وارد شوید:

http://127.0.0.1:8000

🌐 نسخه‌ی آنلاین (Render Deploy)

(https://warehouse-qr-system.onrender.com/)



---
