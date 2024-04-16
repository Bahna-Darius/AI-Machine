# Matplotlib
### putem folosi df.plot() pentru a crea mai multe tipuri de grafice plot, bar, hist, box, kde, area, scatter, hexbin, pie  fara a mai specifica explicit plt.scatter() sau plt.bar(). Pandas permite specificarea tipului de grafic folosind parametrul kind.
### Metoda plot pe care o folosești în Pandas provine din Pandas însuși, nu din Matplotlib. Pandas folosește Matplotlib în spate pentru a crea grafice, dar Pandas oferă o interfață mai simplă și mai intuitivă pentru a crea grafice. Se pot aplica metodele Matplotlib pe obiectele Pandas, dar Pandas oferă o interfață mai simplă și mai intuitivă pentru a crea grafice.

```python
import matplotlib.pyplot as plt

df.plot(kind='scatter', x='column_name_x', y='column_name_y')
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.show()


```

## Tipuri de grafice pe care le poți crea cu df.plot():

1. Line plot: kind='line'
2. Scatter plot: kind='scatter'
3. Bar plot: kind='bar'
4. Histogram: kind='hist'
5. Pie chart: kind='pie'
6. Area plot: kind='area'
7. Box plot: kind='box'
8. Hexbin plot: kind='hexbin'

