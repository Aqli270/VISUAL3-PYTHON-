import PySimpleGUI as sg
sg.theme("Topanga")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ",font=("helvetica",24))],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ",font=("Courier",18,"italic","bold","underline"))],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                           size=(430,200),
                           font=("Times", 18))
window()
window.close()