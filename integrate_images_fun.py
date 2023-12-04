import matplotlib.pyplot as plt
import matplotlib.image as mpimg

images = [
    "./heat map/Agg Assault.jpg",
    "./heat map/Common Assault.jpg",
    "./heat map/Larceny.jpg",
    "./heat map/Rape.jpg",
    "./heat map/Shooting.jpg",
    "./legend_file.png"
]
titles = [
    "Aggravated Assault",
    "Common Assault",
    "Larceny",
    "Rape",
    "Shooting",
    ""
]


fig, axs = plt.subplots(2, 3, figsize=(40, 30))
axs = axs.flatten()


for idx, ax in enumerate(axs):
    if idx < len(images):
        img = mpimg.imread(images[idx])
        ax.imshow(img)
        ax.set_title(titles[idx], fontweight='bold', fontsize=14, pad=10)
        ax.axis('off')
    else:
        ax.axis('off')

plt.subplots_adjust(wspace=0.15, hspace=0.1)

plt.show()
