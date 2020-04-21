import requests
import os


class Speaker:

    url = 'https://translate.google.com/translate_tts'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
    }

    params = {
        'ie': 'UTF-8',
        'client': 'gtx',
    }

    def __init__(self, current_folder='', clip_extension='mp3', language='en'):
        self.current_folder = current_folder
        self.clip_extension = clip_extension
        self.language = language.lower()

    def set_folder(self, current_folder):
        if not os.path.exists(current_folder):
            os.makedirs(current_folder)
        self.current_folder = current_folder

    def set_language(self, language):
        self.language = language.lower()

    def get_clip(self, text_to_speak):
        self.params['q'] = text_to_speak
        self.params['tl'] = self.language
        try:
            r = requests.get(self.url, params=self.params,
                             headers=self.headers)
            return r.content
        except:
            return False

    def get_secure_file_name(self, filename):
        basename, extension = os.path.splitext(filename)
        allowed_chars = 'abcdefghijklmnopqrstuvwxyz_1234567890'  # case-sensitive will ignore
        replace_by_char = '_'
        new_basename = ''.join([(replace_by_char, char)[char.lower() in allowed_chars.lower()]
                                for char in basename])
        return new_basename[:50] + extension

    def save(self, text_to_speak):
        clip_filename = self.get_secure_file_name(
            text_to_speak + '.' + self.clip_extension)
        clip = self.get_clip(text_to_speak)
        if clip:
            try:
                with open(os.path.join(self.current_folder, clip_filename), 'wb') as f:
                    print('Saving in file: ', os.path.join(
                        self.current_folder, clip_filename))
                    f.write(clip)
            except Exception as e:
                print(f"Cannot write file: {clip_filename} -- ({e})")
        else:
            print('ERROR: Nothing to save in file. Try again later.')


if __name__ == "__main__":

    speaker = Speaker()

    speaker.set_language('en')  # en is default
    # folder will be created if doesnt exists
    speaker.set_folder("clips/en")
    speaker.save("What's your name?")
    speaker.save("I'm going to Honolulu tomorrow.")

    speaker.set_language('es')
    speaker.set_folder("clips/es")
    speaker.save('¿A dónde vas?')
    speaker.save('Estoy buscando un restaurante con cuatro gatos.')
