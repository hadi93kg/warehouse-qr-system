from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models.models import Product, Stock
import qrcode
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# ساخت جداول
Base.metadata.create_all(bind=engine)

# صفحه اصلی: لیست محصولات و فرم اضافه کردن
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.post("/add_product")
def add_product(
    name: str = Form(...),
    description: str = Form(None),
    price: int = Form(...),
    db: Session = Depends(get_db)
):
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)

    # تولید QR Code
    qr_path = f"app/static/uploads/product_{product.id}.png"
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    img = qrcode.make(f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}")
    img.save(qr_path)
    product.qr_code_file = qr_path.split("app/")[1]  # مسیر نسبت به static
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# داشبورد با آمار
@app.get("/dashboard")
def dashboard(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    stock_entries = db.query(Stock).all()
    data = {"products": products, "stock": stock_entries}
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})