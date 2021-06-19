#Generate Text to Speech results using IBM Watson™ service
import key
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def speech(text,filename,voice):

    #current audio file name
    save_filename=filename.split('/')[0]+'/'+filename.split('/')[1]+'/'+filename.split('/')[2]+'/audio_'+filename.split('/')[3].split('_')[1].split('.')[0]


    #Pass data to IBM Service
    authenticator = IAMAuthenticator(key.TTS_KEY)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/dd9243e9-d7be-4f1a-9e7a-dd64bc6244c5')

    #Save the output file
    with open(save_filename+'.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice=voice,
                accept='audio/wav'
            ).get_result().content)

