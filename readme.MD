Description
=====

Script allow to convert any text to audio file (mp3) via google translator.


Usage
=====

```python
speaker = Speaker()


speaker.set_language('en')
speaker.set_folder("clips/en")
speaker.save("What's your name?")
# -> clips/en/What_s_your_name_.mp3
speaker.save("I'm going to Honolulu tomorrow.")
# -> clips/en/I_m_going_to_Honolulu_tomorrow_.mp3


speaker.set_language('es')
speaker.set_folder("clips/es")
speaker.save('¿A dónde vas?')
# -> clips/es/_A_d_nde_vas_.mp3
speaker.save('Estoy buscando un restaurante con cuatro gatos.')
# -> clips/es/Estoy_buscando_un_restaurante_con_cuatro_gatos_.mp3
```
