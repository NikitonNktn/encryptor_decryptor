import pyperclip
from tkinter import *
from tkinter import ttk

def show_message():
    input_1 = str(entry.get().lower())
    cipher = {'а': 'sa', 'й': 'sq', 'ц': 'sw', 'у': 'se', 'к': 'sr', 'е': 'st', 'н': 'sy', 'г': 'su', 'ш': 'si', 'щ': 'so', 'з': 'sp',
              'х': 's[', 'ъ': 's]','ф': 'wa','ы': 'ws','в': 'wd','п': 'wt','р': 'wr','о': 'w[','л': 'wq','д': 'wg','ж': 'wh',
              'э': 'wk','я': 'wl','ч': 'wx','с': 'pw','м': 'pq','и': 'po','т': 'py','ь': 'pf','б': 'pd','ю': 'ps','1': 'pc','2': 'pv',
              '3': 'pn','4': 'pm','5': 'pz','6': 'zx','7': 'z]','8': 'zv','9': 'zb','0': 'z>',' ': 'as',',': 'z[','.': 'cv','ё': 'cc',
              
              
              'q': 'aa', 'w': 'aq', 'e': 'aw', 'r': 'ae', 't': 'ar', 'y': 'at', 'u': 'ay', 'i': 'au', 'o': 'ai', 'p': 'ao', 
              '[': 'dp', ']': 'd[','a': 'pa','s': 'ps','d': 'px','f': 'pt','g': 'pr','h': 'p[','j': 'pi','k': 'pg','l': 'ph', 
              ';': 'mk','': 'ml','z': 'mx','x': 'mw','c': 'mq','v': 'mo','b': 'my','n': 'lf','m': 'ld',
              
              } 
    sifr = ""
    
    for i in input_1:
        try:
            sifr += cipher[i]
        except:
             sifr += '☠️☠️' # если в шифровке нет такого символа, то вместо символа будут вставлиы эти эмодзи
    # print(sifr)
    label["text"] = sifr
    pyperclip.copy(sifr)


root = Tk()
root.title("Encoder")
root.geometry("200x200") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="encrypt", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
  
root.mainloop()