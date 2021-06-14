# Fake news classifier

Sencilla web app para correr un clasificador de noticias _fake_ en inglés.

Programada en Python/Flask, se puede ver una demo en [FakeDiy](https://fakediy.herokuapp.com/)

Se corren 3 modelos para clasificar las noticias:

- SVN
- KNN
- RandomForest

La base de datos con etiquetas se descargó del sitio de  [Clément Bisaillon](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset?select=Fake.csv) de [Kaggle](https://www.kaggle.com/)

El modelo para el deploy en Heroku se basó en el desarrollo de [Shaunak Varudandi](https://towardsdatascience.com/fake-news-classifier-to-tackle-covid-19-disinformation-ii-116ed2eb44e4)

El archivo [FakeDiy_Flask.ipynb](https://github.com/matog/FakeDiyClassifier-Flask/blob/main/FakeDiy_Flask.ipynb) es el que genera los "pickles files" con la información de los modelos, para poder hacer la predicción.

_Work in progress_: Conseguir una base etiquetada (FAKE-TRUE) de noticias en español, para entrenar el modelo con contenido local.

![](/img/fake.png)
