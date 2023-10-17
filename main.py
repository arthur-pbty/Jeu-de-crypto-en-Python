import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import numpy as np


crypto_prices = [1000]
ancien_prix = 1000
limite_max = 501
argents = 10000
crypto = 0


def choisir_au_hasard(*args):
    if args:
        return random.choice(args)
    else:
        return None
    

# Fonction pour générer des données de prix crypto avec un bruit gaussien
def generate_crypto_data():
    global ancien_prix, limite_max, crypto_prices, nouveau_prix

    if ancien_prix < 100:
        nouveau_prix = 100
    else:
        nouveau_prix = choisir_au_hasard(
                                         ancien_prix - 1, 
                                         ancien_prix - 1, 
                                         ancien_prix - 1, 
                                         ancien_prix - 1, 
                                         ancien_prix - 1, 
                                         ancien_prix - 2, 
                                         ancien_prix - 2, 
                                         ancien_prix - 2, 
                                         ancien_prix - 5, 
                                         ancien_prix - 5,
                                         ancien_prix - 5,
                                         ancien_prix - 5,
                                         ancien_prix - 10,
                                         ancien_prix - 10,
                                         ancien_prix - 10,
                                         ancien_prix - 10,
                                         ancien_prix - 10,
                                         ancien_prix - 20,
                                         ancien_prix - 20,
                                         ancien_prix - 20,
                                         ancien_prix - 20,
                                         ancien_prix - 30,
                                         ancien_prix - 30,
                                         ancien_prix - 30,
                                         ancien_prix - 40,
                                         ancien_prix - 40,
                                         ancien_prix - 50,
                                         ancien_prix, 
                                         ancien_prix, 
                                         ancien_prix, 
                                         ancien_prix, 
                                         ancien_prix + 1, 
                                         ancien_prix + 1, 
                                         ancien_prix + 1, 
                                         ancien_prix + 1, 
                                         ancien_prix + 1, 
                                         ancien_prix + 2, 
                                         ancien_prix + 2, 
                                         ancien_prix + 2, 
                                         ancien_prix + 5, 
                                         ancien_prix + 5,
                                         ancien_prix + 5,
                                         ancien_prix + 5,
                                         ancien_prix + 10,
                                         ancien_prix + 10,
                                         ancien_prix + 10,
                                         ancien_prix + 10,
                                         ancien_prix + 10,
                                         ancien_prix + 20,
                                         ancien_prix + 20,
                                         ancien_prix + 20,
                                         ancien_prix + 20,
                                         ancien_prix + 30,
                                         ancien_prix + 30,
                                         ancien_prix + 30,
                                         ancien_prix + 40,
                                         ancien_prix + 40,
                                         ancien_prix + 50,
                                         )
    
    #nouveau_prix = random.uniform(ancien_prix - (10/100*ancien_prix), ancien_prix + (10/100*ancien_prix))
    
    
    ancien_prix = nouveau_prix

    crypto_prices.append(nouveau_prix)


    if len(crypto_prices) > limite_max:
        crypto_prices = crypto_prices[-limite_max:]

    
    # Mettre à jour le graphique avec les nouvelles données
    update_graph(crypto_prices)
    
    # Configurer une minuterie pour mettre à jour les données chaque seconde
    root.after(1, generate_crypto_data)


# Fonction pour mettre à jour le graphique
def update_graph(prices):
    ax.clear()
    ax.plot(range(len(prices)), prices, label='Prix Crypto (USD)')
    ax.set_title('Courbe du Prix Crypto')
    ax.set_xlabel('Heures')
    ax.set_ylabel('Prix en USD')
    ax.legend()
    ax.grid(True)
    canvas.draw()

def buy():
    global crypto, argents

    buy_crypto = argents // nouveau_prix
    crypto += buy_crypto

    sell_argents = argents % nouveau_prix
    argents = sell_argents

    print("argents : ", argents)
    print("crypto : ", crypto)


def sell():
    global crypto, argents

    sell_crypto = nouveau_prix * crypto
    argents += sell_crypto

    crypto = 0

    print("argents : ", argents)
    print("crypto : ", crypto)
    

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title('Crypto Viewer')

# Créer une figure Matplotlib
fig, ax = plt.subplots(figsize=(8, 4))

# Créer un widget Canvas Tkinter pour afficher la figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Lancer la génération des données de crypto toutes les secondes
generate_crypto_data()

buy_button = tk.Button(root, text='Acheter', command=buy)
buy_button.pack()

sell_button = tk.Button(root, text='Vendre', command=sell)
sell_button.pack()

# Bouton pour quitter l'application
quit_button = tk.Button(root, text='Quitter', command=root.quit)
quit_button.pack()

# Lancer la boucle principale Tkinter



root.mainloop()
