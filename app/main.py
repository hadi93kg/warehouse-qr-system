# app/main.py
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models.models import Product, Stock
import qrcode
import os
from typing import Optional
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# ساخت جداول
Base.metadata.create_all(bind=engine)

# مطمئن شدن از وجود پوشه uploads
os.makedirs("app/static/uploads", exist_ok=True)

# صفحه اصلی: فرم اضافه کردن محصول و لیست محصولات
@app.get("/", response_class=HTMLResponse)
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

    # تولید و ذخیره QR code
    qr_rel = f"static/uploads/product_{product.id}.png"
    qr_path = os.path.join("app", qr_rel)
    img = qrcode.make(f"product://{product.id}")
    img.save(qr_path)

    product.qr_code_file = qr_rel
    db.commit()

    return RedirectResponse(url="/", status_code=303)

# جزئیات محصول وقتی QR code اسکن شد
@app.get("/product/{product_id}", response_class=HTMLResponse)
def product_detail(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return HTMLResponse("Product not found", status_code=404)
    stock_entries = db.query(Stock).filter(Stock.product_id == product_id).order_by(Stock.timestamp.desc()).all()
    return templates.TemplateResponse("product_form.html", {"request": request, "product": product, "stock_entries": stock_entries})

# داشبورد
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, q: Optional[str] = None, db: Session = Depends(get_db)):
    products_query = db.query(Product)
    if q:
        products_query = products_query.filter(Product.name.contains(q))
    products = products_query.all()
    stock_entries = db.query(Stock).order_by(Stock.timestamp.desc()).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "products": products, "stock_entries": stock_entries})