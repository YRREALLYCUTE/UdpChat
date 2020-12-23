import MainFrame
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame.Server(None)
    frame.Show()
    app.MainLoop()