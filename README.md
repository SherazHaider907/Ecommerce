# Ecommerce Web Application

A full-featured ecommerce platform built with Django. It supports both guest and registered users, with a complete shopping experience from product browsing to order placement.

---

## Features

### Store
- Product catalog with category filtering, search, and pagination
- Product detail page with image gallery, color/size variations, and average rating
- Product reviews and ratings system

### Cart
- Add to cart for both **guest users** (session-based) and **registered users** (account-based)
- Support for product variations (color, size) — same product with different variations tracked separately
- Cart merges automatically when a guest logs in
- Quantity update and item removal

### Orders
- Checkout page with full address and contact form
- Auto-generated order number based on date + order ID
- Tax calculation (2%)
- Order history and order detail view in user dashboard

### Accounts
- Custom user model with email as the login field
- **Email verification** on registration — account activated via link
- **Forgot password** and reset via email token
- Edit profile with profile picture upload
- Change password from dashboard
- User dashboard showing order count and profile info

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, Django Templates
- **Database:** SQLite
- **Image Handling:** Pillow
- **Email:** Django EmailMessage (SMTP)

---

## Project Structure

```
Ecommerce/
├── ECOMMERCE/        # Django project settings & root URLs
├── accounts/         # Custom user model, auth, profile, email verification
├── store/            # Products, variations, reviews, product gallery
├── carts/            # Cart and CartItem (guest + user support)
├── orders/           # Order, OrderProduct, Payment models & views
├── category/         # Category model & context processor
├── templates/        # All HTML templates
│   ├── accounts/     # Login, register, dashboard, profile templates
│   ├── store/        # Store, product detail, cart, checkout
│   ├── orders/       # Payment/confirmation page
│   └── includes/     # Navbar, footer, alerts, sidebar
├── manage.py
└── .env
```

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SherazHaider907/Ecommerce.git
cd Ecommerce
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django pillow
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

> For Gmail, use an **App Password** (not your regular password). Enable 2FA on your Google account, then generate an app password from your Google account settings.

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

---

## Key URLs

| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/store/` | All products |
| `/store/<category>/` | Products by category |
| `/store/<category>/<product>/` | Product detail |
| `/cart/` | Shopping cart |
| `/cart/checkout/` | Checkout page |
| `/orders/place_order/` | Place order |
| `/accounts/register/` | Register |
| `/accounts/login/` | Login |
| `/accounts/dashboard/` | User dashboard |
| `/accounts/my_orders/` | Order history |
| `/accounts/edit_profile/` | Edit profile |
| `/admin/` | Django admin panel |
