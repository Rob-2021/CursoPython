from textblob import TextBlob

class AnaliadorSentimientos:
    def analizar_sentimientos(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "Positivo"
        elif analisis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negativo"

analizador = AnaliadorSentimientos()
resultado = analizador.analizar_sentimientos('Hola como estas?')
print(resultado)