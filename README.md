# EDA-calidad_google_cloud_translate
# Evaluación de la calidad de la traducción automática de Google del inglés al español, rumano, francés, italiano y danés.

## 1. Introducción
  En este EDA se pretende analizar la calidad de la traducción automática de Google Cloud Translate tras la integración de IA en textos de naturaleza jurídica.
  
  Nota importante: las traducciones solo se van a analizar desde un punto de vista de métricas computacionales, índice BLEU, índice Meteor, ratio TER y número de ediciones, sin que haya una evaluación por parte de un traductor de la calidad.
  
 ## 2. Hipótesis nulas
 ### 2.1. Cuanto más largos y complejos sean los fragmentos de texto, peor es la calidad de las traducciones generadas por ordenador.
 ### 2.2. Cuanto menos flexivo es un idioma desde un punto de vista morfológico, mayor es la calidad de las traducciones automáticas.
 
 ## 3. Desarrollo
  Primero se han recopilado 20 textos jurídicos de diferente temática separados y alineados en columnas en fragmentos de diferentes longitud. Se ha decidido finalmente hacer la separación por fragmentos por la nueva incorporación de la mejora de la traducción de Google por el contexto en la actualización en la que ha agregado IA a su traductor, en columnas separadas para el texto original y cada idioma./nLuego se ha pasado a realizar la traducción del texto en inglés a cada uno de los idiomas elegidos, usando la APi de Google Cloud Translate.
  
  A continuación, se ha procesado el texto, se pre-tokenizado y se ha añadido una nueva columna con la cantidad de palabras de cada fragmento.
  
  Posteriormente, utilizando las librería nlkt, sacrebleu y Levenstein, se han añadido columnnas nuevas para cada idioma con el cálculo del índice BLEU, Meteor, TER y número de ediciones para cada idioma.
  
  Una vez obtenido el Dataframe y guardado en formato csv, se ha pasado al análisis de datos.
  
  En primer lugar, se han analizado los índices de las traducciones y se ha visualizado en mapas de calor la correlación con la longitud de las frases.
  
  En segundo lugar, se han analizadolos mismos datos, visualizando en gráficos de dispersión los índices de calidad y el número de ediciones para cada idioma.
  
  En tercer lugar, se ha realizado una segunda visualización de estos datos en gráficos de barras, pero esta vez generando para cada idioma gráficos separados para cada idioma dividiendo los fragmentos en dos grupos, cortos y largos, mostrango mínimo, media y máximo de la puntuación obtenida en cada caso y la varianza de los datos.
  
  En cuarto lugar, se han ordenado los idiomas de menor a mayor grado de flexión morfológica, teniendo en cuenta declinaciones de sustantivos, adjetivos, verbos y pronombres.
  
  Por último, se han generado gráficos de líneas de de la media de los datos sobre calidad obtenidos.
  
## 4. Conclusiones
  Tras, hay que rechazar la primera hipótesis que indice que la calidad de las traducciones de fragmentos más largos son de peor calidad que la de las fragmentos cortos. Observamos que la calidad mejora a medida que el traductor automático recibe más contexto.
  
Sin embargo, a medida que los fragmentos se van alejando y van siendo más complejos, la calidad se situa en torno al 0,8 calculada con el índice BLEU, en torno al 0,72 calculada con el índice Meteor, en torno a 105 con el índice TER y las ediciones se disparan a unas 350 para los fragmentos largos.

Por tanto, podemos afirmar que en frases cortas la calidad de la traducción automática puede variar ampliamente. Un índice de calidad de 0 indica una traducción muy deficiente, mientras que un índice de calidad de 1 indica una traducción perfecta.

A medida que las fragmentos se hacen más largos, el modelo de traducción automática tiene más contexto para trabajar y puede producir traducciones más consistentes. El hecho de que el índice de calidad se estabilice en un rango específico, como 0.65 a 0.93 en el caso del índice BLEU, puede indicar que el modelo tiende a producir traducciones de bastante calidad en fragmentos largos, pero siempre con un espacio de mejora. Si además nos fijamos en el índice METEOR, que tiene en cuenta más aspectos, como la correctitud gramatical, la ordenación de las palabras y contempla casos de sinonimia, observamos que en este caso el rango se amplia y cuenta con valores de entre 0.45 y 0.93. Por tanto, a pesar de que la traducción automática va mejorando conforme reciba máx contexto, en ningún caso se alcanza ya la "traducción perfecta" que en ocasiones puede llegar a alcanzar en fragmentos cortos.

  Se rechaza también la segunda hipótesis. No hay una relación clara entre la flexión de los idiomas y la calidad de su traducción automática. Según el índice BLEU incluso podemos ver que se produce el efecto contrario. Por tanto, rechazamos la hipótesis.
  
Este año Google ha integrado IA a su traductor y parece que hay idiomas como el rumano, que ha resultado muy beneficiado por esta incorporación y que según el índice BLEU recibe la mejor puntuación pesar de ser el idioma más flexivo.

En cuanto al índice Meteor, que contempla la correción gramatical y la sinonímia de palabras, y que se suele considerar que más próximo a una evaluación humana de la traducción que el BLEU, vemos que el español es el que obtiene mejores resultados con diferencia. Un factor que podría influir en este resultado es el gran contenido de texto que hay en Internet. Según Internet World Stats, en 2020, los usuarios del español en Internet es de 7.9%, el del francés de 3,3 y el resto no aparecen entre los diez idiomas con mayor número de usuarios, por tanto su uso es de menos de un 2%.

### Fuentes:
https://eur-lex.europa.eu/homepage.html
https://www.internetworldstats.com/
