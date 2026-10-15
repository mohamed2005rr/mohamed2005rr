import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# =========================
# إعداد الشكل
# =========================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# =========================
# قاعدة البيانات
# =========================
conn = sqlite3.connect("delivery.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    phone TEXT PRIMARY KEY
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT,
    order_text TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()

# =========================
# تسجيل مستخدم
# =========================
def register():
    phone = phone_entry.get()

    if phone == "":
        messagebox.showwarning("خطأ", "ادخل رقم التليفون")
        return

    try:
        cursor.execute("INSERT INTO users VALUES (?)", (phone,))
        conn.commit()
        messagebox.showinfo("تم", "تم التسجيل بنجاح")
    except:
        messagebox.showerror("خطأ", "الرقم مسجل بالفعل")

# =========================
# تسجيل دخول
# =========================
def login():
    phone = phone_entry.get()

    cursor.execute("SELECT * FROM users WHERE phone=?", (phone,))
    user = cursor.fetchone()

    if user:
        open_orders_window(phone)
    else:
        messagebox.showerror("خطأ", "المستخدم غير موجود")

# =========================
# نافذة الأوردرات
# =========================
def open_orders_window(phone):
    win = ctk.CTkToplevel(root)
    win.title("Orders")

    ctk.CTkLabel(win, text=f"Welcome: {phone}", font=("Arial", 16)).pack(pady=10)

    order_entry = ctk.CTkEntry(win, width=300, placeholder_text="اكتب الأوردر")
    order_entry.pack(pady=10)

    order_list = ctk.CTkTextbox(win, width=350, height=150)
    order_list.pack(pady=10)

    # إضافة أوردر
    def add_order():
        text = order_entry.get()

        cursor.execute(
            "INSERT INTO orders (phone, order_text, status) VALUES (?, ?, ?)",
            (phone, text, "Pending")
        )
        conn.commit()

        messagebox.showinfo("تم", "تم إضافة الأوردر")
        show_orders()

    # عرض الأوردرات
    def show_orders():
        order_list.delete("1.0", "end")

        cursor.execute("SELECT id, order_text, status FROM orders WHERE phone=?", (phone,))
        orders = cursor.fetchall()

        for o in orders:
            order_list.insert("end", f"#{o[0]} | {o[1]} | {o[2]}\n")

    # قبول الأوردر
    def accept_order():
        order_id = id_entry.get()
        cursor.execute("UPDATE orders SET status='Accepted' WHERE id=?", (order_id,))
        conn.commit()
        messagebox.showinfo("تم", "تم قبول الأوردر")
        show_orders()

    # تسليم الأوردر
    def deliver_order():
        order_id = id_entry.get()
        cursor.execute("UPDATE orders SET status='Delivered' WHERE id=?", (order_id,))
        conn.commit()
        messagebox.showinfo("تم", "تم تسليم الأوردر")
        show_orders()

    ctk.CTkButton(win, text="➕ إضافة أوردر", command=add_order).pack(pady=5)

    ctk.CTkButton(win, text="📋 عرض الأوردرات", command=show_orders).pack(pady=5)

    id_entry = ctk.CTkEntry(win, width=200, placeholder_text="رقم الأوردر")
    id_entry.pack(pady=10)

    ctk.CTkButton(win, text="✅ قبول الأوردر", command=accept_order).pack(pady=5)

    ctk.CTkButton(win, text="📦 تم التسليم", command=deliver_order).pack(pady=5)

# =========================
# الواجهة الرئيسية
# =========================
root = ctk.CTk()
root.title("Delivery App")
root.geometry("350x300")

ctk.CTkLabel(root, text="🚚 Delivery App", font=("Arial", 20)).pack(pady=15)

phone_entry = ctk.CTkEntry(root, width=250, placeholder_text="رقم التليفون")
phone_entry.pack(pady=10)

ctk.CTkButton(root, text="📝 تسجيل", command=register).pack(pady=5)

ctk.CTkButton(root, text="🔓 دخول", command=login).pack(pady=5)

root.mainloop()