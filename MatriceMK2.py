import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



def Matrice(MS):
    s=10
    liste1=[]
    liste2=[]
    liste3=[]
    liste4=[]
    liste5=[]
    print(MS)
    for i in range(10,60):
        if i <20:
            MS[i]=MS[i]
            liste1.append(MS[i])
        if i>=20 and i<30:
            MS[i]=MS[i]
            liste2.append(MS[i])
            MS[i]=MS[i]
        if i>=30 and i<40:
            MS[i]=MS[i]
            liste3.append(MS[i])
        if i>=40 and i<50:
            MS[i]=MS[i]
            liste4.append(MS[i])
        if i>=50 and i<60:
            MS[i]=MS[i]
            liste5.append(MS[i])
    print("JE SUIS UNIQUE")
    print(MS)
    Matrice=[]
    Matrice.append(liste1)
    Matrice.append(liste2)
    Matrice.append(liste3)
    Matrice.append(liste4)
    Matrice.append(liste5)
    print("JE SUIS ENCORE PLUS UNIQUE")
    print(Matrice)
    return(Matrice)
    


methods = [None, 'none', 'lanczos']

grid = Matrice()

fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(80, 40),
                        subplot_kw={'xticks': [], 'yticks': []})

fig.subplots_adjust(left=0.03, right=0.97, hspace=0.3, wspace=0.05)

for ax, interp_method in zip(axs.flat, methods):
    
    ax.imshow(grid, interpolation=interp_method, cmap="plasma", norm = mpl.colors.Normalize(vmin=20.,vmax=60))
    ax.set_title(str(interp_method))


plt.tight_layout()
plt.show()
