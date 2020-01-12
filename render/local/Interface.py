import wx

APP_EXIT = 1



class Interface(wx.Frame):

    def __init__(self, parent, title):
        super(Interface, self).__init__(parent=parent, title=title, size=(800, 600))
        self.InitUI()
        self.Center()

    def InitUI(self):
        None


    def onOK(self, event):
        # Do something
        print
        'onOK handler'

    def onCancel(self, event):
        self.closeProgram()

    def closeProgram(self):
        self.Close()


    def MenuBar(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')

        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        fileMenu.AppendSubMenu(imp, 'I&mport')

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)

    def OnQuit(self, e):
        self.Close()



def main():
    app = wx.App()
    interface = Interface(None, title="Manager")
    interface.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
