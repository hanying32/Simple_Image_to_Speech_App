#Generate Optical Character Recognition Result from Free OCR API
import re
import requests

# Get the corresponding language parameter name in each services from the user input
def language_table(language):

    #user_language_input:{OCR_input,TTS_input}
    language_dict = {
        'Arabic': ['ara', 'ar-AR_OmarVoice'],
        'Chinese(Simplified)': ['chs', 'zh-CN_LiNaVoice'],
        'Chinese(Traditional)': ['cht', 'zh-CN_ZhangJingVoice'],
        'Dutch': ['dut', 'nl-NL_EmmaVoice'],
        'English': ['eng', 'en-US_AllisonV3Voice'],
        'French': ['fre', 'fr-FR_NicolasV3Voice'],
        'German': ['ger', 'de-DE_ErikaV3Voice'],
        'Korean': ['kor', 'ko-KR_YunaVoice'],
        'Italian': ['ita', 'it-IT_FrancescaV3Voice'],
        'Japanese': ['jpn', 'ja-JP_EmiV3Voice'],
        'Portuguese': ['por', 'pt-BR_IsabelaV3Voice'],
        'Spanish': ['spa', 'es-LA_SofiaVoice'],
    }
    if language=='Language':#User didn't choose any language, use the default value
        return language_dict['Chinese(Traditional)'][0],language_dict['Chinese(Traditional)'][1]
    else:
        return language_dict[language][0],language_dict[language][1]

#remove unwanted part just keep the detected text
def data_preprocess(fulltext):

    start_str='"ParsedText":'
    end_str='"ErrorMessage"'
    start_index = fulltext.find(start_str) + len(start_str)
    end_index=fulltext.find(end_str)
    text=fulltext[start_index:end_index-1]
    new_text=re.sub(r'[\\r\\n\\"]', '', text)
    return new_text


#Generate the OCR result
def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
            Python3.5 - not tested on 2.7
        :param filename: Your file path & name.
        :param overlay: Is OCR.space overlay required in your response.
                        Defaults to False.
        :param api_key: OCR.space API key.
                        Defaults to 'helloworld'.
        :param language: Language code to be used in OCR.
                        List of available language codes can be found on https://ocr.space/OCRAPI
                        Defaults to 'en'.
        :return: Result in JSON format.
        """
    #get the correct language parameter name
    language,voice=language_table(language)
    #call the Free OCR API
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'detectOrientation':True
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    #get the ocr text result
    text=data_preprocess(r.text)
    print(text)
    if text=='':
        print(filename," no output")
    return text,voice