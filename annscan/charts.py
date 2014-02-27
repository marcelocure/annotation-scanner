import matplotlib.pyplot as plt


def generate_chart(total_files, occurrencies):
    labels = 'With @Refactoring', 'Without @Refactoring'
    sizes = [total_files, occurrencies]
    colors = ['yellowgreen', 'gold', ]
    explode = (0, 0.1)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=False, startangle=180)
    plt.axis('equal')
    plt.savefig('chart.png')
    plt.show()
