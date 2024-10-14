
import wx

def bind(widget, event):
    def decorator(func):
        print(help(wx.GetTopLevelParent))
        f = wx.GetTopLevelParent(widget)
        f.Bind(event, func, widget)
        return func
    return decorator


if __name__ == "__main__":
    app = wx.App(False)

    frame = wx.Frame(None, wx.ID_ANY, "Event binding with decorators")
    frame.Show(True)

    panel = wx.Panel(frame)
    sizer = wx.BoxSizer(wx.VERTICAL)

    lb = wx.ListBox(panel, choices=['one', 'two', 'three', 'four'], style=wx.LB_SINGLE)
    sizer.Add(lb)

    panel.SetSizer(sizer)
    panel.Fit()

    @bind(lb, wx.EVT_LISTBOX)
    def onselect(evt):
        w = evt.EventObject
        print(f"You selected item {w.Selections}: {w.StringSelection}")

    app.MainLoop()

