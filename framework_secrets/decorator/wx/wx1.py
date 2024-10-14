
import wx


class MyButton(wx.Button):
    def command(self, func):
        self.GrandParent.Bind(wx.EVT_BUTTON, func, self)
        return func

if __name__ == "__main__":
    app = wx.App(False)

    frame = wx.Frame(None, wx.ID_ANY, "Event binding with decorators")
    frame.Show(True)

    panel = wx.Panel(frame)
    sizer = wx.BoxSizer(wx.HORIZONTAL)

    btn1 = MyButton(panel, label="one")
    btn2 = MyButton(panel, label="two")

    sizer.Add(btn1)
    sizer.Add(btn2)

    panel.SetSizer(sizer)
    panel.Fit()

    @btn1.command
    @btn2.command
    def onclick(event):
        print(f"You clicked on button <{event.EventObject.Label}>")

    app.MainLoop()

