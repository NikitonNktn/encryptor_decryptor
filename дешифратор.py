import pyperclip
from tkinter import *
from tkinter import ttk
def show_message():
    input_2 = str(entry.get().lower())
    cipherof = {'а': 'sa', 'й': 'sq', 'ц': 'sw', 'у': 'se', 'к': 'sr', 'е': 'st', 'н': 'sy', 'г': 'su', 'ш': 'si', 'щ': 'so', 'з': 'sp',
              'х': 's[', 'ъ': 's]','ф': 'wa','ы': 'ws','в': 'wd','п': 'wt','р': 'wr','о': 'w[','л': 'wq','д': 'wg','ж': 'wh',
              'э': 'wk','я': 'wl','ч': 'wx','с': 'pw','м': 'pq','и': 'po','т': 'py','ь': 'pf','б': 'pd','ю': 'ps','1': 'pc','2': 'pv',
              '3': 'pn','4': 'pm','5': 'pz','6': 'zx','7': 'z]','8': 'zv','9': 'zb','0': 'z>',' ': 'as',',': 'z[','.': 'cv','ё': 'cc',
              
              
              'q': 'aa', 'w': 'aq', 'e': 'aw', 'r': 'ae', 't': 'ar', 'y': 'at', 'u': 'ay', 'i': 'au', 'o': 'ai', 'p': 'ao', 
              '[': 'dp', ']': 'd[','a': 'pa','s': 'ps','d': 'px','f': 'pt','g': 'pr','h': 'p[','j': 'pi','k': 'pg','l': 'ph', 
              ';': 'mk','': 'ml','z': 'mx','x': 'mw','c': 'mq','v': 'mo','b': 'my','n': 'lf','m': 'ld',
              
              } 
    cipher =   dict(zip(cipherof.values(), cipherof.keys()))
    
    sifr = ""
    
    for i in range(0, len(input_2), 2):
        try:
            sifr += cipher[(input_2[i:i+2])]
        except:
             sifr += '☠️☠️'
    label["text"] = sifr
    # print(sifr)
    pyperclip.copy(sifr)
    

root = Tk()
root.title("Decoder")
root.geometry("200x200") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="decipher", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
  
root.mainloop()
