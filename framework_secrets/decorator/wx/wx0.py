
import wx

def onclick(event):  # requires an event argument unlike Tkinter
    print("You clicked a button")


if __name__ == "__main__":
    app = wx.App(False)

    frame = wx.Frame(None, wx.ID_ANY, "Event binding with decorators")
    frame.Show(True)

    panel = wx.Panel(frame)
    sizer = wx.BoxSizer(wx.HORIZONTAL)

    btn1 = wx.Button(panel, label="one")
    btn2 = wx.Button(panel, label="two")

    sizer.Add(btn1)
    sizer.Add(btn2)

    panel.SetSizer(sizer)
    panel.Fit()

    frame.Bind(wx.EVT_BUTTON, onclick, btn1)
    frame.Bind(wx.EVT_BUTTON, onclick, btn2)

    app.MainLoop()

