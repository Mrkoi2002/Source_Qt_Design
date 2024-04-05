# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
from Qt_Core import *

# IMPORT PAGES
from Gui.Pages.Pages import Ui_Application_Pages

# IMPORT CUSTOM WIDGETS
from Gui.Widgets.Py_Push_Button import PyPushButton
from Gui.Widgets.Py_Push_Button_Top import PyPushButton_Top



# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        # ///////////////////////////////////////////////////////////////
        parent.resize(1280, 720)
        parent.setMinimumSize(960, 540)

        # Trước khi hiển thị cửa sổ, đặt cờ Qt.FramelessWindowHint
        


            

        # CREATE CENTRAL WIDGET
        # ///////////////////////////////////////////////////////////////
        self.Central_Frame = QFrame()

        # CREATE MAIN LAYOUT
        self.Main_Layout = QHBoxLayout(self.Central_Frame)
        self.Main_Layout.setContentsMargins(0,0,0,0)
        self.Main_Layout.setSpacing(0)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        self.Left_Menu = QFrame()
        self.Left_Menu.setStyleSheet("background-color: #44475a")
        self.Left_Menu.setMaximumWidth(50)
        self.Left_Menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.Left_Menu_Layout = QVBoxLayout(self.Left_Menu)
        self.Left_Menu_Layout.setContentsMargins(0,0,0,0)
        self.Left_Menu_Layout.setSpacing(0)

        # TOP FRAME MENU
        self.Left_Menu_Top_Frame = QFrame()
        self.Left_Menu_Top_Frame.setMinimumHeight(40)
        self.Left_Menu_Top_Frame.setObjectName("Left_Menu_Top_Frame")
        

        # TOP FRAME LAYOUT
        self.Left_Menu_Top_Layout = QVBoxLayout(self.Left_Menu_Top_Frame)
        self.Left_Menu_Top_Layout.setContentsMargins(0,0,0,0)
        self.Left_Menu_Top_Layout.setSpacing(0)


       


        # TOP BTNS
        self.Button_Toggle = PyPushButton(
            text = "Hide Menu",
            icon_path = "icon_menu.svg"
        )
        self.Button_Home = PyPushButton(
            text = "Home",
            is_active = True,
            icon_path = "icon_home.svg"
        )
        self.Button_File = PyPushButton(
            text = "File",
            icon_path = "icon_folder.svg"
        )

        # ADD BTNS TO LAYOUT
        self.Left_Menu_Top_Layout.addWidget(self.Button_Toggle)
        self.Left_Menu_Top_Layout.addWidget(self.Button_Home)
        self.Left_Menu_Top_Layout.addWidget(self.Button_File)
       

        # MENU SPACER
        # ///////////////////////////////////////////////////////////////
        self.Left_Menu_Spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        # ///////////////////////////////////////////////////////////////
        self.Left_Menu_Bottom_Frame = QFrame()
        self.Left_Menu_Bottom_Frame.setMinimumHeight(40)
        self.Left_Menu_Bottom_Frame.setObjectName("Left_Menu_Bottom_Frame")
       

        self.Left_Menu_Bottom_Layout = QVBoxLayout(self.Left_Menu_Bottom_Frame)
        self.Left_Menu_Bottom_Layout.setContentsMargins(0,0,0,0)
        self.Left_Menu_Bottom_Layout.setSpacing(0)

        # BOTTOM BTNS
        self.Button_Setting = PyPushButton(
            text = "Settings",
            icon_path = "icon_settings.svg"
        )


        self.Left_Menu_Bottom_Layout.addWidget(self.Button_Setting)

        
        # # ADD BTNS TO LAYOUT
        # self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # LABEL VERSION
        # ///////////////////////////////////////////////////////////////
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # ADD TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.Left_Menu_Layout.addWidget(self.Left_Menu_Top_Frame)
        self.Left_Menu_Layout.addItem(self.Left_Menu_Spacer)
        self.Left_Menu_Layout.addWidget(self.Left_Menu_Bottom_Frame)
        self.Left_Menu_Layout.addWidget(self.left_menu_label_version)

        
        # CONTENT
        # ///////////////////////////////////////////////////////////////
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
      

        # TOP BAR
        # ///////////////////////////////////////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(0,0,0,0)
        self.top_bar_layout.setSpacing(0)
        



       


         # LEFT TOP LABEL
        self.top_label_left = QLabel("CHECK IN")

        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        

         # TOP BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.top_bar_frame = QFrame()
        self.top_bar_frame.setObjectName("top_bar_frame")
        
        


        self.top_bar_frame_layout = QHBoxLayout(self.top_bar_frame)
        self.top_bar_frame_layout.setContentsMargins(0,0,0,0)
        self.top_bar_frame_layout.setSpacing(0)


        #  # TOP BTNS
        # self.Close_Button = QPushButton("Home")
        # self.Close_Button.setMaximumWidth(30)
        # self.Minimize_Button = QPushButton("File")
        # self.Maximize_Button = QPushButton("Language")

        # TOP BTNS

        self.Close_Button = PyPushButton_Top(
            icon_path = "icon_close.svg"
        )

        self.Minimize_Button = PyPushButton_Top(
            icon_path = "icon_minimize.svg"
        )

        self.Maximize_Button = PyPushButton_Top(
            icon_path = "icon_maximize.svg"
        )

        # Chỉnh kích thước các nút Close, Maximize và Minimize thành 30x30 pixel
        


        # ADD BTNS TO LAYOUT
        self.top_bar_frame_layout.addWidget(self.Close_Button)
        self.top_bar_frame_layout.addWidget(self.Minimize_Button)
        self.top_bar_frame_layout.addWidget(self.Maximize_Button)

        # ADD TO TOP BAR LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_bar_frame)


        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")
        self.ui_pages = Ui_Application_Pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.Home_Pages)
        
        
        # BOTTOM BAR
        # ///////////////////////////////////////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)


        # LEFT BOTTOM LABEL
        self.bottom_label_left = QLabel("TIME............")

        # BOTTOM SPACER
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # RIGHT BOTTOM LABEL
        self.bottom_label_right = QLabel("© 2024")

        # ADD TO BOTTOM BAR LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        

        

        # ADD TO CONTEN LAYOUT

        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
       

        # ADD WIDGETS TO APP
        # ///////////////////////////////////////////////////////////////
        self.Main_Layout.addWidget(self.Left_Menu)
        self.Main_Layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.Central_Frame)