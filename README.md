# 🎂 ANAÏS - Smart Order Management System

A custom-built, lightweight CRM and Order Management solution designed specifically for local pastry shops and small businesses to replace traditional paper-based systems.

## 🚀 The Problem
Many local businesses (like the "ANAΪΣ" pastry shop) struggle with handwritten orders, manual weight-to-price calculations, and the time-consuming process of notifying customers when their orders are ready.

## 💡 The Solution
This web application digitizes the entire workflow:
* **Order Logging:** Quickly capture customer details, delivery dates, and custom cake designs (with image uploads).
* **Auto-Calculation:** Automatically calculates the final balance (Total Price - Down Payment) based on the actual weight of the product.
* **Smart Viber Integration:** One-click notification system that opens a pre-filled Viber message with the customer's specific order details and remaining balance.

## 🛠️ Tech Stack
* **Backend:** Python & Flask
* **Database:** SQLite3
* **Frontend:** Bootstrap 5 (Responsive UI)
* **Communication:** Viber URI Scheme Integration

## 📸 Features
* **Status Management:** Separate views for "Pending" and "Completed" orders.
* **Visual Tracking:** Support for uploading reference images for custom cake designs.
* **Mobile Friendly:** Optimized for use on tablets and smartphones within the shop.
* **Copy-to-Clipboard Fallback:** Ensures 100% reliability for customer notifications even if browser-to-app communication is restricted.

## 🛠️ Installation & Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/ganotisp-maker/anais-pastry-app.git](https://github.com/ganotisp-maker/anais-pastry-app.git)
