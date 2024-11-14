import PySimpleGUI as sg
sg.theme("Topanga")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS", 
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM : 2210010633")],
                           [sg.Text("Nama : Muhammad Aqli Andi Basith")],
                           [sg.Text("Kelas : 5E Regular Banjarmasin")],
                           [sg.Text("Matkul : Pemrograman Visual 3")],
                           ],
                   size=(500,500),
                   font=("Times",18))
window()
window.close()