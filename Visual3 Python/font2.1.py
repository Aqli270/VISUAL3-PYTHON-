import PySimpleGUI as sg
sg.theme("Topanga")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                           size=(400,200),
                           font=("Times", 18))
window()
window.close()