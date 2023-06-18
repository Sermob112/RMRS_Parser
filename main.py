import  Parser
import sys
soup = 0
from Parser import *
from Interface import *

def parse_wrapper():
    print(path)
    par = Parser()
    par.get_links()
    par.all_info(window)
    par.execl_maker(path)



def application():
    global window
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()

    def handle_save_file_dialog():
        global path
        path = window.saveFileDialog()

    window.SelectCatalog.clicked.connect(handle_save_file_dialog)
    window.ParseBut.clicked.connect(parse_wrapper)



    sys.exit(app.exec_())
if __name__ == '__main__':
    application()
