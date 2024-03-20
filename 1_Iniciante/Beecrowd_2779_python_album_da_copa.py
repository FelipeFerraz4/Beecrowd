album = int(input())
figures = int(input())
albumFigure = []
for i in range(figures):
    figure = int(input())
    if (figure in albumFigure) == False:
        albumFigure.append(figure)
print(album - len(albumFigure))