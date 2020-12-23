import MainFrame
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame.Client(None)
    frame.Show()
    app.MainLoop()