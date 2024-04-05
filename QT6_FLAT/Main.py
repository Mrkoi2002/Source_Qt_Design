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

# IMPORT MODULES
import sys
import os 

# IMPORT QT CORE
from Qt_Core import *

# IMPORT MAIN WINDOW
from Gui.Windows.Main_Window.Ui_Main_Window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CHECK IN")
        # Trước khi hiển thị cửa sổ, đặt cờ Qt.FramelessWindowHint
        self.setWindowFlags(Qt.FramelessWindowHint)

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        self.show()

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)


        # TOGGLE BUTTON

        self.ui.Button_Toggle.clicked.connect(self.Toggle_Button)

         # HOME BUTTON
        self.ui.Button_Home.clicked.connect(self.Show_Home_Pages)

        # FILE BUTTON
        self.ui.Button_File.clicked.connect(self.Show_File_Pages)



    # RESET BTN SELECTION
    def reset_selection(self):
        for btn in self.ui.Left_Menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    # BTN HOME FUNCTION
    def Show_Home_Pages(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Home_Pages)
        self.ui.Button_Home.set_active(True)

    # BTN FILE FUNCTION
    def Show_File_Pages(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.File_Pages)
        self.ui.Button_File.set_active(True)

    # # BTN SETTINGS FUNCTION
    # def Show_Setting_Pages(self):
    #     self.reset_selection()
    #     self.ui.pages.setCurrentWidget(self.ui.ui_pages.Setting_Pages)
    #     self.ui.Button_Setting.set_active(True)


    


    # TOGGLE BUTTON
    def Toggle_Button(self):
        # Get menu width
        Menu_Full = self.ui.Left_Menu.width()

        # Check with
        Width = 50
        if Menu_Full == 50:
            Width = 200

        # Start animation
        self.animation = QPropertyAnimation(self.ui.Left_Menu, b"minimumWidth")
        self.animation.setStartValue(Menu_Full)
        self.animation.setEndValue(Width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())