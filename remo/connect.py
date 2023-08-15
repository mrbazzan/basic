import urllib.request
import urllib.error
import tkinter as tk


def test_connectivity():
  window = tk.Tk()
  window.geometry('600x400')
  head = tk.Label(window, text='Connectivity Checker')
  head.pack(pady=20)

  def check_url():
      web = (url.get())
      status_code = urllib.request.urlopen(web).getcode()
      website_is_up = status_code == 200

      if website_is_up:
          wbs_lbl["text"] = "Website Available"
      else:
          wbs_lbl["text"] = "Website Not Available"


  url = tk.StringVar()
  tk.Entry(window, textvariable=url).place(x=200, y=80, height=30, width=280)
  tk.Button(window, text='Check', command=check_url).place(x=285, y=150)

  wbs_lbl = tk.Label(
    window,
    font=('Calibri 15')
  )
  wbs_lbl.place(x=260, y=200)

  window.mainloop()


if __name__ == '__main__':
  test_connectivity()
