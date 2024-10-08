from back import Database

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtGui import QScreen

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,                       
    QPushButton,
    QTableWidget,
    QTableWidgetItem,   
    QHeaderView,
    QLineEdit,
    QScrollArea, 
    QSpinBox, 
    QMessageBox,
    QFrame,
)

class AboutPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setStyleSheet("""
            background-color: #fff;
            font-size: 30px;
        """)
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        screen_width = screen.width()
        screen_height = screen.height()

        self.resize(screen_width, screen_height)

        self.v_box = QVBoxLayout()

        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(50, 10, 50, 10)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # logo bolimi
        self.logo_lebel = QLabel(self)
        self.logo_lebel.setStyleSheet("""
            QLabel{
                background-color: #424c59
            }
        """)
 
        pixmap = QPixmap('logo.png')
        self.logo_lebel.setPixmap(pixmap)
        self.logo_lebel.setAlignment(Qt.AlignmentFlag.AlignCenter)
 

        self.title = QLabel("""
            <div style="text-align: center;line-height:0.8;">
                <p style="font-size: 28px; font-weight:bold; color: #00838f;">Dorixona dasturlari boshqaruvchilari va foydalanuvchilari uchun ro'yxatdan o'tish</p>
                <p style="font-size: 26px; font-weight:bold; color: #00838f;"> va da'vo qilish uchun mo'ljallangan portalga xush kelibsiz!</p>
            </div>
        """)
        self.title.setStyleSheet("color: #00838f")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.line_lebel = QLabel()

        pixline = QPixmap('line.png')
        self.line_lebel.setPixmap(pixline)
        self.line_lebel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.enter_button = QPushButton("Kirish")
        self.enter_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 4px ridge #f1f2f3;
                border-radius: 12px;
                padding: 10px 25px;
                width: 150px
            }
            QPushButton:hover {
                background-color: #2980b9
            }
        """)
        self.enter_button.clicked.connect(self.def_login)

        self.info_title = QLabel("""
            <div style="text-align: left; width: 100%; line-height:0;">
                <h3>Dori-Darmonlar Bo'yicha Imtiyozlar:</h3>
                <hr>
                <ul>
                    <li><b>Bepul Dori-Darmonlar:</b> Ehtiyojmand keksa odamlar va nogironlar uchun davlat tomonidan belgilangan ro'yxatdagi ayrim dori-darmonlar bepul taqdim etiladi.</li>
                    <li>Pensiya va ijtimoiy nafaqa oluvchilar uchun ayrim dori-darmonlar bepul yoki subsidiyalangan narxda taqdim etiladi.</li>
                </ul>
            </div>
            <div style="text-align: left; width: 100%; line-height:0;">
                <h3 >Bepul Davolanish Bo'yicha Imtiyozlar:</h3>
                <hr>
                <ul>
                    <li><b>Davlat Tibbiy Xizmatlari:</b> Davlat tomonidan moliyalashtiriladigan poliklinikalar va gospitalarda keksa odamlar va nogironlar uchun bepul tibbiy xizmatlar ko'rsatiladi.</li>
                    <li>Keksalar va nogironlar uchun umumiy terapevtik xizmatlar, diagnostika tahlillari va laboratoriya tekshiruvlari bepul taqdim etiladi.</li>
                    <li><b>Maxsus Tibbiy Xizmatlar:</b> Keksalar va nogironlar uchun reabilitatsiya markazlarida bepul davolanish va fizioterapiya xizmatlari ko'rsatiladi.</li>
                </ul>
            </div>
        """)
        self.info_title.setStyleSheet("font-size: 18px; color: #333333;")
        self.info_title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        form_layout.addWidget(self.logo_lebel)
        form_layout.addWidget(self.title)
        form_layout.addWidget(self.line_lebel)
        form_layout.addWidget(self.enter_button, alignment=Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.info_title)

        self.v_box.addLayout(form_layout)

        self.setLayout(self.v_box)

        # scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)
        # scroll_content = QWidget()
        # scroll_content.setLayout(self.v_box)
        # scroll_area.setWidget(scroll_content)

        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(scroll_area)

        # self.setLayout(main_layout)

    def def_login(self):
        self.close()
        self.login = LoginPage()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Database()
        self.showMaximized()
        self.setWindowTitle("Login Page")
        self.setStyleSheet("""
            background-color: #fff;
            font-size: 30px
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # Logo va title uchun layout
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_logo_label = QLabel(self)
        self.login_logo_label.setFixedWidth(1000)
        self.login_logo_label.setStyleSheet("""
            QLabel{
                background-color: #424c59;
            }
        """)
        pixmapl = QPixmap("logo.png")
        self.login_logo_label.setPixmap(pixmapl)
        self.login_logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.login_logo_label,0,Qt.AlignmentFlag.AlignCenter)

        self.login_title = QLabel("Platformaga kirish")
        self.login_title.setStyleSheet("""
            QLabel{
                background-color: #14808d;
            }
        """)
    # self.login_title.setFont(QFont("Poppins", 32, QFont.Weight.Medium))
        self.login_title.setStyleSheet("color: #F9E400")
        self.login_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.login_title)
    # Login va parol uchun form layout
        form_layout1 = QVBoxLayout()
        form_layout1.setContentsMargins(0, 0, 0, 0)
        form_layout1.setSpacing(20)
        form_layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_layout = QHBoxLayout()
        self.login_label = QLabel("Login:")
        self.login_label.setMinimumWidth(100)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("""
            background-color: #2d3137;
            color: white;
            font-size: 25px;
            padding: 10px 25px 10px 25px;
            border: 4px ridge #f1f2f3;
            border-radius: 12px;
        """)
        self.login_input.setPlaceholderText("👤 Loginni kiriting...")
        self.login_input.setFixedWidth(300)

        login_layout.addStretch()
        login_layout.addWidget(self.login_label)
        login_layout.addWidget(self.login_input)
        login_layout.addStretch()
        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        form_layout1.addLayout(login_layout)

        password_layout = QHBoxLayout()
        self.password_label = QLabel("Parol:")
        self.password_label.setMinimumWidth(100)
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("""
            background-color: #2d3137;
            color: white;
            font-size: 25px;
            padding: 10px 25px 10px 25px;
            border: 4px ridge #f1f2f3;
            border-radius: 12px;
        """)
        self.password_input.setPlaceholderText("🔒 Parolni kiriting...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedWidth(300)

        password_layout.addStretch()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)
        password_layout.addStretch()
        password_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout1.addLayout(password_layout)

        self.info_label = QLabel()
    # Login tugmasi
        self.login_button = QPushButton("Login")
        self.login_button.setMaximumWidth(300)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 4px ridge #f1f2f3;
                border-radius: 12px;
                padding: 10px 25px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        form_layout1.addWidget(self.login_button,0,Qt.AlignmentFlag.AlignCenter)

        # form_layout1.addWidget(self.login_button)
        # self.login_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_button.clicked.connect(self.handle_login)

        social_layout = QHBoxLayout()
        social_layout.setContentsMargins(0, 30, 0, 0)
        social_layout.setSpacing(25)

        self.forget_button = QPushButton("Parolni tiklash")
        self.forget_button.setStyleSheet("""
            background-color: #FFDB00;
            color: #AF47D2;
            padding: 10px;
            border-radius: 3px;
            font-size: 14px;
        """)
        self.forget_button.setFixedWidth(200)

        self.registration_button = QPushButton("Ro'yxatdan o'tish")
        self.registration_button.setStyleSheet("""
            background-color: #FFDB00;
            color: #AF47D2;
            padding: 10px;
            border-radius: 3px;
            font-size: 14px;
        """)
        self.registration_button.setFixedWidth(200)

        self.registration_button.clicked.connect(self.registr)

        social_layout.addStretch(2)
        social_layout.addWidget(self.forget_button)
        social_layout.addStretch(1)
        social_layout.addWidget(self.registration_button)
        social_layout.addStretch(2)

        form_layout1.addLayout(social_layout)
        form_layout.addLayout(form_layout1)
        main_layout.addLayout(form_layout)

        # Asosiy layoutni o'rnatamiz
        self.setLayout(main_layout)

    def handle_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login:
            self.login_input.setPlaceholderText("To'ldirilmagan")
        if not password:
            self.password_input.setPlaceholderText("To'ldirilmagan")

        if login and password:
            user = {
                'login': login,
                'password': password
            }

            role = self.core.get_id(user)
            if role =='admin':
                self.close()
                self.admin = AdminPage()
            elif role =='user':
                self.close()
                self.user = UserPage()
            else:
                print("Invalid login credentials")

    def registr(self):
        self.close()
        self.registration = RegistrationPage()

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Registration")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px;
            background-color: #bdd2e2;
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Login kiriting")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Parol kiriting")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.telnumber_input = QLineEdit()
        self.telnumber_input.setPlaceholderText("Telefon nomer kiriting")

        self.info_label = QLabel()

        self.save_btn = QPushButton("Saqlash")
        self.save_btn.clicked.connect(self.create_user)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("""
            background-color: #f44336;
            color: #ffffff;
            padding: 10px;
            font-size: 20px;
            border-radius: 5px;
            cursor: pointer
        """)
        self.back_button.clicked.connect(self.back)

        self.v_box.addStretch(80)
        self.v_box.addWidget(self.login_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(40)
        self.v_box.addWidget(self.back_button, 0,Qt.AlignmentFlag.AlignCenter )

        self.setLayout(self.v_box)
        self.show()

    def create_user(self):
        self.info_label.clear()
        login = self.login_input.text()
        password = self.password_input.text()

        if login and password:
            user = {
                'login': login,
                'password': password,
            }
            err = self.core.insert_user(user)
            if err:
                self.info_label.setText("Bunday login mavjud")
            else: 
                self.info_label.setText("Muvaffaqiyatli ro'yxatdan o'tdingiz")
        else:
            self.info_label.setText("Barcha bandlarni to'ldiring")

    def back(self):
        self.close()
        self.login = LoginPage()

class AdminPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Mehnat-1")
        self.showMaximized()
        self.setStyleSheet('background-color: #BBE9FF')

        main_widget = QWidget()
        main_layout = QHBoxLayout()

        self.sidebar_layout = QVBoxLayout()
        sidebar_items = [
            "Mijoz",
            "Ta'minotchi",
            "Xarid va tolov",  
            "Sotuv va Tolov",
            "Adminlar",
            "Kategoriya", 
            "Maxsulot"
        ]

        self.sidebar_buttons = []
        for i, item in enumerate(sidebar_items):
            button = QPushButton(item)
            button.setStyleSheet("""
                QPushButton {
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    padding: 10px;
                    background-color: #f0f0f0;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:checked {
                    background-color: #d0d0d0;
                }
            """)
            button.setCheckable(True)
            button.clicked.connect(lambda _, idx=i: self.display_content(idx))
            self.sidebar_buttons.append(button)
            self.sidebar_layout.addWidget(button)

        self.stacked_widget = QStackedWidget()

        self.stacked_widget.addWidget(self.create_customer_page())
        self.stacked_widget.addWidget(self.create_supplier_page())
        self.stacked_widget.addWidget(self.create_purchase_payment_page())
        self.stacked_widget.addWidget(self.create_sale_payment_page())
        self.stacked_widget.addWidget(self.create_users_page())
        self.stacked_widget.addWidget(self.create_category_page())
        self.stacked_widget.addWidget(self.create_product_page())

        main_layout.addLayout(self.sidebar_layout, 1)
        main_layout.addWidget(self.stacked_widget, 3)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.show()

    def display_content(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def create_customer_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        employee_frame = QFrame()
        employee_frame.setFrameShape(QFrame.Shape.Box)
        employee_frame.setFrameShadow(QFrame.Shadow.Raised)
        employee_frame.setLineWidth(2)
        employee_layout = QVBoxLayout(employee_frame)

        employee_title = QLabel("Registered Employees")
        employee_title.setStyleSheet("font-weight: bold; font-size: 16px;")
        employee_layout.addWidget(employee_title)

        self.employee_list = QListWidget()
        self.populate_employee_list()
        employee_layout.addWidget(self.employee_list)

        button_layout = QHBoxLayout()
        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected_employee)
        view_button = QPushButton("View Details")
        view_button.clicked.connect(self.view_employee_details)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(view_button)
        
        employee_layout.addLayout(button_layout)

        layout.addWidget(employee_frame)
        widget.setLayout(layout)
        
        return widget

    def populate_employee_list(self):
        data = self.core.get_all_info()

        self.employee_list.clear()
        for employees in data:
            name, id_info, department = employees
            item_text = f"{name}\n{id_info}\nPhone number: {department}"
            self.employee_list.addItem(item_text)

    def delete_selected_employee(self):
        selected_items = self.employee_list.selectedItems()

        if selected_items:
            for item in selected_items:
                self.core.delete_employee(item.text().split('\n')[1])
                self.employee_list.takeItem(self.employee_list.row(item))

    def view_employee_details(self):
        selected_items = self.employee_list.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            employee_info = selected_item.text()
            self.show_employee_details(employee_info)

    def show_employee_details(self, info):
        from PyQt6.QtWidgets import QMessageBox
        details_dialog = QMessageBox(self)
        details_dialog.setWindowTitle("Employee Details")
        details_dialog.setText(f"Details:\n{info}\n\nPurchase history information would be here.")
        details_dialog.exec()
        
        return self.create_page_widget("Mijozlar sahifasi")

    def create_supplier_page(self):
        widget = self.create_page_widget("Ta'minotchilar sahifasi")

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Ta'minotchi")
        search_button = QPushButton("Search")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)

        supplier_list = QListWidget()
        supp_data = self.core.suppliers_info()

        for suppliers in supp_data:
            name, phone = suppliers
            item = QListWidgetItem(f"{name}\n{phone}")
            supplier_list.addItem(item)

        layout = widget.layout()
        layout.addLayout(search_layout)
        layout.addWidget(supplier_list)

        return widget

# ------------------------------------------------------------
    # def create_purchase_payment_page(self):
    def create_purchase_payment_page(self):
        widget = QWidget()
        layout = QHBoxLayout()

        xarid_widget = self.create_xarid_section()
        taminotchiga_tolov_widget = self.create_taminotchiga_tolov_section()
        bugungi_xaridim_widget = self.create_bugungi_xaridim_section()

        layout.addWidget(xarid_widget)
        layout.addWidget(taminotchiga_tolov_widget)
        layout.addWidget(bugungi_xaridim_widget)

        widget.setLayout(layout)
        return widget

    def create_xarid_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Xarid")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(4, 4)
        table.setHorizontalHeaderLabels(["Ta'minotchi", "Sana", "Xarid savatim", "Tami"])
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_taminotchiga_tolov_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Taminotchiga to'lov")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(2, 2)
        table.setHorizontalHeaderLabels(["Ta'minotchi", "To'lov"])
        layout.addWidget(table)
        
        add_button = QPushButton("To'lash")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_bugungi_xaridim_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Bugungi xaridim")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(0, 3)  # Start with 0 rows
        table.setHorizontalHeaderLabels(["Ta'minotchi", "Sana", "Xarid"])
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame
    
        # return self.create_page_widget("Xarid va tolov sahifasi")

    # ---------------------------------------------------
    # def create_sale_payment_page(self):
        # return self.create_page_widget("Sotuv va tolov sahifasi")

    def create_sale_payment_page(self):
        widget = QWidget()
        layout = QHBoxLayout()

        sotuv_widget = self.create_sotuv_section()
        bugungi_sotuv_widget = self.create_bugungi_sotuv_section()
        tolov_widget = self.create_tolov_section()

        layout.addWidget(sotuv_widget)
        layout.addWidget(bugungi_sotuv_widget)
        layout.addWidget(tolov_widget)

        widget.setLayout(layout)
        return widget

    def create_sotuv_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Sotuv")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Sana", "Summa"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        data = self.core.customers_info()

        for row, val in enumerate(data):
            val = list(val)
            val[1],val[2] = str(val[1]),str(val[2])
            customer, date, amount = val
            table.setItem(row, 0, QTableWidgetItem(customer))
            table.setItem(row, 1, QTableWidgetItem(date))
            table.setItem(row, 2, QTableWidgetItem(amount))
        
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_bugungi_sotuv_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Bugungi sotuv")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(0, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Sana", "Summa"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(table)

        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_tolov_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("To'lov")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Summa", "Sana"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        data = self.core.customers_info()

        for row, val in enumerate(data):
            val = list(val)
            val[1],val[2] = str(val[1]),str(val[2])
            customer, date, amount = val
            table.setItem(row, 0, QTableWidgetItem(customer))
            table.setItem(row, 1, QTableWidgetItem(amount))
            table.setItem(row, 2, QTableWidgetItem(date))
            
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            
            for icon_name in ["trash", "edit", "undo", "redo", "print"]:
                button = QPushButton()
                button.setIcon(QIcon(f"path/to/{icon_name}_icon.png"))
                action_layout.addWidget(button)

            table.setCellWidget(row, 3, action_widget)

        layout.addWidget(table)

        add_button = QPushButton("+ To'lash")
        layout.addWidget(add_button)

        frame.setLayout(layout)
        return frame

    # -------------------------------------------------
    # def create_users_page(self):
    #     """Create the Users page widget."""
    #     return self.create_page_widget("Adminlar sahifasi")

    def create_users_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Foydalanuvchilar")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Foydalanuvchilar")
        search_button = QPushButton(QIcon("path/to/search_icon.png"), "")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.users_table = QTableWidget()
        self.users_table.setColumnCount(4)
        self.users_table.setHorizontalHeaderLabels(["Name", "Email", "Role", "Actions"])
        self.users_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.populate_admins_table()
        layout.addWidget(self.users_table)

        add_user_button = QPushButton("+ Yangi foyd...")
        add_user_button.clicked.connect(self.add_new_user)
        layout.addWidget(add_user_button, alignment=Qt.AlignmentFlag.AlignRight)

        widget.setLayout(layout)
        return widget

    def populate_admins_table(self):
        admins_data = self.core.admins_info()

        self.users_table.setRowCount(len(admins_data))

        for row, val in enumerate(admins_data):
            val = list(val)
            val[1] = str(val[1])
            name, email, role = val
            self.users_table.setItem(row, 0, QTableWidgetItem(name))
            self.users_table.setItem(row, 1, QTableWidgetItem(email))
            self.users_table.setItem(row, 2, QTableWidgetItem(role))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            info_button = QPushButton(QIcon("path/to/info_icon.png"), "")
            info_button.clicked.connect(lambda _, r=row: self.show_user_info(r))
            action_layout.addWidget(info_button)

            self.users_table.setCellWidget(row, 3, action_widget)

    def show_user_info(self, row):
        _id = self.users_table.item(row, 1).text()
        name = self.users_table.item(row, 0).text()
        role = self.users_table.item(row, 2).text()

        print(f"User Info: {_id}, {name}, {role}")

    def add_new_user(self):
        print("Adding a new user")
    

    # ----------------------------------------------------

    # def create_category_page(self):
    #     """Create the Category page widget."""
    #     return self.create_page_widget("Kategoriya sahifasi")

    def create_category_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Kategoriya")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.categories_table = QTableWidget()
        self.categories_table.setColumnCount(3)
        self.categories_table.setHorizontalHeaderLabels(["Icon", "Name", "Actions"])
        self.categories_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.categories_table.verticalHeader().setVisible(False)
        self.populate_categories_table()
        layout.addWidget(self.categories_table)

        add_category_button = QPushButton("Kategoriya qo'shish")
        add_category_button.clicked.connect(self.add_new_category)
        layout.addWidget(add_category_button, alignment=Qt.AlignmentFlag.AlignRight)

        widget.setLayout(layout)
        return widget

    def populate_categories_table(self):
        categories_data = self.core.get_midicine_category()
        self.categories_table.setRowCount(len(categories_data))

        # print(categories_data)
        for row, val in enumerate(categories_data):
            category, image = val
            icon_label = QLabel()
            icon_label.setPixmap(QIcon(image).pixmap(24, 24))
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.categories_table.setCellWidget(row, 0, icon_label)

            self.categories_table.setItem(row, 1, QTableWidgetItem(category))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            view_button = QPushButton(QIcon("path/to/view_icon.png"), "")
            edit_button = QPushButton(QIcon("path/to/edit_icon.png"), "")
            action_layout.addWidget(view_button)
            action_layout.addWidget(edit_button)

            self.categories_table.setCellWidget(row, 2, action_widget)

    def add_new_category(self):
        print("Adding a new category")
    
# -----------------------------------------------------
    # def create_product_page(self):
    #     """Create the Product page widget."""
    #     return self.create_page_widget("Maxsulot sahifasi")

    def create_product_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title = QLabel("Maxsulotlar")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        add_product_button = QPushButton("+ Maxsulot qo'shish")
        add_product_button.clicked.connect(self.add_new_product)
        title_layout.addWidget(title)
        title_layout.addStretch()
        title_layout.addWidget(add_product_button)
        layout.addLayout(title_layout)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Maxsulotlarni qidirish")
        search_button = QPushButton(QIcon("path/to/search_icon.png"), "")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.products_table = QTableWidget()
        self.products_table.setColumnCount(6)
        self.products_table.setHorizontalHeaderLabels(["Rasm", "Nomi", "Kategoriyasi", "Miqdori", "Narxi", "Amallar"])
        self.products_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.products_table.verticalHeader().setVisible(False)
        self.populate_products_table()
        layout.addWidget(self.products_table)

        widget.setLayout(layout)
        return widget

    def populate_products_table(self):
        products_data = self.core.get_all_medics_info()
        self.products_table.setRowCount(len(products_data))
        
        for row, val in enumerate(products_data):
            name, category, quantity, price, image = val
            
            image_label = QLabel()
            image_label.setPixmap(QIcon(image).pixmap(32, 32))
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.products_table.setCellWidget(row, 0, image_label)

            self.products_table.setItem(row, 1, QTableWidgetItem(name))
            self.products_table.setItem(row, 2, QTableWidgetItem(category))
            self.products_table.setItem(row, 3, QTableWidgetItem(str(quantity)))
            self.products_table.setItem(row, 4, QTableWidgetItem(str(price)))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            view_button = QPushButton(QIcon("path/to/view_icon.png"), "")
            edit_button = QPushButton(QIcon("path/to/edit_icon.png"), "")
            delete_button = QPushButton(QIcon("path/to/delete_icon.png"), "")
            action_layout.addWidget(view_button)
            action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            self.products_table.setCellWidget(row, 5, action_widget)

    def add_new_product(self):
        print("Adding a new product")

    def create_page_widget(self, title):
        widget = QWidget()
        layout = QVBoxLayout()
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(2)

        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(QLabel(title))
        frame.setLayout(frame_layout)

        layout.addWidget(frame)
        widget.setLayout(layout)
        return widget

class UserPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Capsule Pharmacy")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            background-color: #F0F0F0;
            font-size: 16px;
        """)
        
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.addWidget(self.main_widget)

        self.create_header()
        self.create_search_bar()
        self.create_menu_buttons()
        self.create_special_offers()
        self.create_medicine_table()
        self.create_bottom_menu()

        self.cart_page = QWidget()
        self.cart_layout = QVBoxLayout(self.cart_page)
        self.create_cart_page()
        self.central_widget.addWidget(self.cart_page)

        self.cart_items = []

        self.show()

    def create_header(self):
        header_layout = QHBoxLayout()
        logo_label = QLabel("Capsule Pharmacy")
        logo_label.setStyleSheet("color: #e08946; font-size: 24px; font-weight: bold;")
        phone_label = QLabel("8-97-777-77-77")
        header_layout.addWidget(logo_label)
        header_layout.addWidget(phone_label, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_layout.addLayout(header_layout)

    def create_search_bar(self):
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Maxsulot va toifalarni kiriting")
        search_button = QPushButton("Qidirish")
        search_button.clicked.connect(self.search_items)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        self.main_layout.addLayout(search_layout)

    def search_items(self):
        search_text = self.search_input.text().lower()
        for row in range(self.table.rowCount()):
            item_name = self.table.item(row, 0).text().lower()
            item_price = self.table.item(row, 1).text().lower()
            if search_text in item_name or search_text in item_price:
                self.table.setRowHidden(row, False)
            else:
                self.table.setRowHidden(row, True)

    def create_menu_buttons(self):
        menu_layout = QHBoxLayout()
        buttons = ["SAVATCHA", "BONUSLAR", "BUYURTMALAR"]
        for text in buttons:
            button = QPushButton(text)
            button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
            if text == "SAVATCHA":
                button.clicked.connect(self.show_cart_page)
            menu_layout.addWidget(button)
        self.main_layout.addLayout(menu_layout)

    def create_special_offers(self):
        count = self.core.add_up_medics()
        offers_label = QLabel(f"Mavjud maxsulotlar soni: {count}")
        offers_label.setStyleSheet("color: #e08946; font-weight: bold;")
        self.main_layout.addWidget(offers_label)

    def create_medicine_table(self):
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Nomi", "Narxi", "Soni", ""])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        medicines = self.core.medicine_info()

        for val in medicines:
            name, amount, price = val
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(price)))
            self.table.setItem(row, 2, QTableWidgetItem(str(amount)))

            quantity_spinbox = QSpinBox()
            quantity_spinbox.setMinimum(1)
            quantity_spinbox.setMaximum(100)
            self.table.setCellWidget(row, 2, quantity_spinbox)
            
            add_to_cart_btn = QPushButton("Savatga joylash")
            add_to_cart_btn.clicked.connect(lambda _, r=row: self.add_to_cart(r))
            self.table.setCellWidget(row, 3, add_to_cart_btn)
        
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table)
        scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(scroll_area)

    def add_to_cart(self, row):
        medicine_name = self.table.item(row, 0).text()
        price = float(self.table.item(row, 1).text())  # Convert price to float
        quantity_spinbox = self.table.cellWidget(row, 2)  # Get the quantity spinbox widget
        quantity = quantity_spinbox.value()  # Get the selected quantity

        if quantity > 0:
            self.cart_items.append((medicine_name, price, quantity))  # Add item to cart with quantity
            # print(f"Savatga qo'shildi: {medicine_name} - {price} so'm, Soni: {quantity}")
        else:
            QMessageBox.warning(self, "Ogohlantirish", "Soni 0 dan katta bo'lishi kerak!")

    def create_cart_page(self):
        back_button = QPushButton("Orqaga")
        back_button.clicked.connect(self.show_main_page)
        self.cart_layout.addWidget(back_button)

        cart_label = QLabel("Mening savatim")
        cart_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.cart_layout.addWidget(cart_label)

        self.cart_table = QTableWidget(0, 3)
        self.cart_table.setHorizontalHeaderLabels(["Nomi", "Narxi", "Soni"])
        self.cart_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.cart_layout.addWidget(self.cart_table)

        buy_button = QPushButton("Sotib olish")
        buy_button.clicked.connect(self.process_purchase)
        self.cart_layout.addWidget(buy_button)
    
    def process_purchase(self):
        if not self.cart_items:
            QMessageBox.information(self, "Xabar", "Savatingiz bo'sh!")
        else:
            request = []
            
            total = 0
            for name, price, quantity in self.cart_items:
                total+=price * quantity
                request.append((quantity,name))

            answer = self.core.remove_medics(request)

            if answer:
                message = answer
                QMessageBox.information(self, "Xatolik", message)
                self.cart_items.clear()
            else:
                message = f"Jami summa: {total} so'm\nXaridingiz uchun rahmat!"
                QMessageBox.information(self, "Xarid yakunlandi", message)
                self.cart_items.clear()
                self.update_cart_table()

    def show_cart_page(self):
        self.update_cart_table()
        self.central_widget.setCurrentWidget(self.cart_page)

    def show_main_page(self):
        self.central_widget.setCurrentWidget(self.main_widget)

    def update_cart_table(self):
        self.cart_table.setRowCount(0)
        for item in self.cart_items:
            row = self.cart_table.rowCount()
            self.cart_table.insertRow(row)
            self.cart_table.setItem(row, 0, QTableWidgetItem(item[0]))
            self.cart_table.setItem(row, 1, QTableWidgetItem(f"{item[1]} so'm"))
            self.cart_table.setItem(row, 2, QTableWidgetItem(str(item[2])))

    def create_bottom_menu(self):
        bottom_menu = QHBoxLayout()
        icons = ["home.png", "menu.png", "cart.png", "phone.png", "user.png"]
        for icon in icons:
            button = QPushButton()
            button.setIcon(QIcon(icon))
            bottom_menu.addWidget(button)
        self.main_layout.addLayout(bottom_menu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AboutPage()
    window.show()
    sys.exit(app.exec())