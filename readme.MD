Description
=====

Script allow to convert any text to audio file (mp3) via google translator.

Idea from:
https://www.youtube.com/watch?v=ruAownOJJKA


Usage
=====

```python
speaker = Speaker()


speaker.set_language('en')
speaker.set_folder("clips/en")
speaker.save("What's your name?")
speaker.save("I'm going to Honolulu tomorrow.")


speaker.set_language('es')
speaker.set_folder("clips/es")
speaker.save('¿A dónde vas?')
speaker.save('Estoy buscando un restaurante con cuatro gatos.')
```
