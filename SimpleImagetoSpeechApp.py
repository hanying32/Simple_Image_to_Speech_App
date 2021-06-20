#App Design
import OCR
import TTS
import key
import os,shutil
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label



photo_count=0#counts of taking pictures
root='./save/'#directory to collect the raw data and the result data
photo_dir=root+'img/'#folder to save all the photoes to be processed
audio_dir = root + 'audio/'#folder to save the audio results



#Screen for Choosing Files
class FileChooserScreen(Screen):

    #Photo Preview : show the currently selected photo on the right side
    def selected(self, filename):

        try:
            self.ids.image.source = filename[-1]
        except:
            pass

    #File Arrangement : Copy all the uploaded files to the same folder
    def copy_file(self, filename):

        global photo_dir,photo_count

        if not os.path.exists(root):
            os.mkdir(root)
        if os.path.exists(photo_dir):
            shutil.rmtree(photo_dir)
        os.mkdir(photo_dir)
        for i,img in enumerate(filename):
            try:
                shutil.copy(img, photo_dir+"IMG_"+str(i)+"."+img.split('.')[-1])
                photo_count+=1
            except:
                print(img+' error')
                pass



#Final Screen : Show Results
class CompleteScreen(Screen):

    #Play the audio result after pressing the button
    def play_audio(self,file):

        global audio_dir
        sound = SoundLoader.load(audio_dir+file)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    '''
    Generate the Final Screen:
        1.Show buttons if there are available data
        2.Show "No Output Files" if no output texts were generated
    '''
    def gen_final_screen(self):

        global audio_dir,photo_count

        if os.path.exists(audio_dir):
            layout = GridLayout(cols=2)
            self.add_widget(layout)
            for file in os.listdir(audio_dir):
                layout.add_widget(Button(text=file, on_press=lambda sender, file=file:self.play_audio(file)))

        else:
            layout = AnchorLayout()
            self.add_widget(layout)
            lbl = Label(text='No Output Files')
            layout.add_widget(lbl)

    #Generate the text from the photos
    def TTS_process(self,text,filename,voice):

        global root,audio_dir

        if not os.path.exists(audio_dir):
            os.mkdir(audio_dir)
        TTS.speech(text, audio_dir+filename,voice)

    #Generate the text from the photos
    def OCR_process(self,language):

        global root,photo_dir,audio_dir

        if os.path.exists(audio_dir):
            shutil.rmtree(audio_dir)
        if photo_count==0:
            shutil.rmtree(photo_dir)
        else:
            for f in os.listdir(photo_dir):
                text,voice = OCR.ocr_space_file(filename=photo_dir+f,language=language,api_key=key.OCR_KEY)
                if text !="":
                    self.TTS_process(text,f,voice)
        self.gen_final_screen()



#Camera Screen
class CameraClickScreen(Screen):

    #Take photoes
    def capture(self):

        global photo_count,root,photo_dir

        if not os.path.exists(root):
            os.mkdir(root)
        camera = self.ids['camera']
        if not os.path.exists(photo_dir):
            os.mkdir(photo_dir)
        else:#remove old data
            if photo_count==0:
                shutil.rmtree(photo_dir)
                os.mkdir(photo_dir)
        camera.export_to_png(photo_dir+"IMG_{}.png".format(photo_count))
        photo_count+=1
        print("Captured")



#Star Screen : For users to choose the detected language and the mode to upload photos ( either select from existed files or take photoes )
class StartScreen(Screen):
    pass



#The App
class TextReader(App):

    def build(self):
        GUI=Builder.load_file('./simple_img_speech.kv')
        return GUI

TextReader().run()
