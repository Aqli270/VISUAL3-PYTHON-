import PySimpleGUI as sg
window = sg.Window(title="Latihan Pertama",
                   layout=[[sg.Text("NPM : 2210010633")],
                           [sg.Text("Nama : Muhammad Aqli Andi Basith")],
                           [sg.Text("Kelas : 5E Regular Banjarmasin")],
                           [sg.Text("Matkul : Pemrograman Visual 3")],
                           ],
                   size=(400,200))
window()
window.close()