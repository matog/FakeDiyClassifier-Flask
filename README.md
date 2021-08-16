# Fake news classifier

Sencilla web app para correr un clasificador de noticias _fake_ en español.

Programada en Python/Flask. Se puede usar una demo en [FakeDiy](https://fakediyspanish.herokuapp.com/)

Se corren 3 modelos para clasificar las noticias:

- SVN
- KNN
- RandomForest

La base de datos con etiquetas se descargó del repositorio de [JPPosadas](https://github.com/jpposadas/FakeNewsCorpusSpanish)

El modelo para el deploy en Heroku se basó en el desarrollo de [Shaunak Varudandi](https://towardsdatascience.com/fake-news-classifier-to-tackle-covid-19-disinformation-ii-116ed2eb44e4)

La base de noticias para entrenar el modelo no es extensa, por lo que las predicciones no son del todo precisas. Por lo que se ve, tiene mayoría de fuentes españolas y mexicanas. Las noticias con modismos de esos paises funcionan mejor a la hora de la predicción.


![](https://user-images.githubusercontent.com/660448/122110466-f3be9580-cdf4-11eb-8e3b-380e70ec2d69.png)
