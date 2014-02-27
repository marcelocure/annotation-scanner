import matplotlib.pyplot as plt


def generate_chart(total_files, occurrencies):
    labels = 'Annotation occurrencies', 'Files without annotation'
    sizes = [total_files, occurrencies]
    colors = ['yellowgreen', 'gold', ]
    explode = (0.2, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    #plt.axis('equal')
    plt.savefig('chart.png')
    plt.show()
