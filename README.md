# Simple image to speech app
 Simple image to speech app implemented with the IBM Watson™ Text to Speech API and OCR.space Free OCR API.

## Table of contents
* [Build process](#build-process)
* [Introduction](#introduction)
* [Details of the approach](#details-of-the-approach)
* [Results](#results)
* [Reference](#reference)

## Build process

Project is created with:

    
 * __Python 3.8__ 
 * __Kivy 2.0.0__
 * __IBM Watsons Service__ 
 
    ```pip install --upgrade "ibm-watson>=5.2.0"```

    Get free API key here:https://cloud.ibm.com/apidocs/text-to-speech
    
 * __OCR.space Free OCR API__ 
 
    Get free API key here: https://ocr.space/OCRAPI

You need a working camera for image capturing.

Please update the key.py with your own api keys.

Execute SimpleImagetoSpeechApp.py for start running the app.


## Introduction

### Why I develop this app

To make good use of time, I would like to read books while doing exercise or prepare for the exams of the day while riding on the bus. However, it's really hard for me to keep my eyes on the book while dealing with other things simultaneously. I started to think maybe these tasks would be done easily by listening not reading, and doing things by listening could put to good use for people who want or need to have more time to rest their eyes. Therefore, I want to write my own simple image to speech app even though there are already many powerful apps for the same purpose on the market. 



### Usage
This app helps users to read the text in the image, 
and it's able to deal with 11 different languages as listed below:
    Arabic,Chinese(Simplified/Traditional),Dutch,English,French,German,Korean,Italian,Japanese,Portuguese,Spanish



### Background material
* __OCR.space Free OCR API__

    OCR.space Free OCR API can detect the text in the image. It'll provide the result it recognized. The service is free for 25,000 requests per month.(for more information:https://ocr.space/OCRAPI)
    
* __IBM Watson™ Text to Speech API__
    
    IBM Watson™ Text to Speech API helps us turn the text in to an audio. I registered the IBM lite account which provides free text to speech service with 10000 words per month.
(for more information:https://cloud.ibm.com/catalog/services/text-to-speech)








## Details of the approach
### Process 
Choose language -> Upload Photo ->  Optical Character Recognition  ->  Text-to-Speech  -> Play Audio Files
### Details of each process
* __Choose language__

    The default is set to "Chinese(Traditional)". There are 11 common languages that both OCR.space Free OCR API and IBM Watson™ Text to Speech API can cope with.
    

    
* __Upload Photo__

    Users can upload image from files or take photos by camera. The default file path is set to the project's directory. Users can upload multiple files at once, and  the files selected will be copied to the default file ( ex : project's path/save/img/ ) and be remamed with the order of selection (count from 0, ex : project's path/save/img/IMG_0.jpg ).
    

* __Optical Character Recognition__

    OCR.space Free OCR API is applied for detecting the text in the image, after receiving an image it'll return the text it recognized.If there are no words being recognized, the program will skip the text to speech process. 
    
    Let's take this photo as an example:
  
    ![test-ch1](https://user-images.githubusercontent.com/34962951/122667783-2f879f80-d1e7-11eb-8ea4-fb79a62edd22.jpg)
  
    The following text is what we've got:
  
    ```
    {"ParsedResults":[{"TextOverlay":{"Lines":[],"HasOverlay":false,"Message":"Text overlay is not provided as it is not requested"},"TextOrientation":"0","FileParseExitCode":1,"ParsedText":"生物生存的氣體。這些發現,讓人們對火星充滿了想像。\r\n大海;星球周圍有薄薄的「大氣層」圍繞著,似乎有能提供\r\n望這顆閃耀著暗紅色光芒的星體。在天文學家的觀察中,發\r\n星球上可能有水氣;地表的陰影,顯示上頭有高山、深谷和\r\n現火星有許多跟地球類似的地方:火星南北極有冰冠,代表\r\n從古代開始,人們就依靠著肉眼或者各種觀測工具,遙\r\n他們成功的把重達九百公斤、史上最重的行星探測器送上火\r\n火星探測器好奇號成功登陸火星地表。一分鐘後,美國太\r\n星,為人類探索外太空寫下重要的\r\n空總署的控制中心傳出了歡呼,工作人員開心的擁抱著。\r\n西元二○一二年美東時間八月六日凌晨一點三十一分,\r\n里程碑。\r\n凌登署控斤碑\r\n","ErrorMessage":"","ErrorDetails":""}],"OCRExitCode":1,"IsErroredOnProcessing":false,"ProcessingTimeInMilliseconds":"2328","SearchablePDFURL":"Searchable PDF not generated as it was not requested."}
    ```

    However, only the "ParsedText" field is what we need and there are some useless line breaks in the result.

    After removing the useless parts, we get our final result:
    ```
     生物生存的氣體。這些發現,讓人們對火星充滿了想像。大海;星球周圍有薄薄的「大氣層」圍繞著,似乎有能提供望這顆閃耀著暗紅色光芒的星體。在天文學家的觀察中,發星球上可能有水氣;地表的陰影,顯示上頭有高山、深谷和現火星有許多跟地球類似的地方:火星南北極有冰冠,代表從古代開始,人們就依靠著肉眼或者各種觀測工具,遙他們成功的把重達九百公斤、史上最重的行星探測器送上火火星探測器好奇號成功登陸火星地表。一分鐘後,美國太星,為人類探索外太空寫下重要的空總署的控制中心傳出了歡呼,工作人員開心的擁抱著。西元二○一二年美東時間八月六日凌晨一點三十一分,里程碑。凌登署控斤碑   
    ```
* __Text-to-Speech__

    IBM Watson™ Text to Speech API does the job for turning text in to speech, which generates an audio file as the output. The output files are saved in the folder ( ex : project's path/save/audio/ ) and the files will be named by the image name( ex : IMG_0.jpg -> audio0.wav ). There are several voices for each language in the IBM service, and I've set them to the ones I prefer. The audio files format I use is '.wav', you can change them to different format too.


 * __Play Audio Files__
 
    There will be buttons on the screen for you to play the generated audio files. But If there're no audio files generated, the screen will show up with the text "No Output Files". 
 
 
## Results

* Initial Screen:

  ![startscreen](https://user-images.githubusercontent.com/34962951/122667781-2dbddc00-d1e7-11eb-8836-908e2f65c0d6.JPG)

* Language Selection:

  ![language](https://user-images.githubusercontent.com/34962951/122667773-2696ce00-d1e7-11eb-9896-06aca5ccac17.JPG)

* File Chooser: 

  _The file which is  being selected will show up on the right window._
    
  ![preview](https://user-images.githubusercontent.com/34962951/122667779-2ac2eb80-d1e7-11eb-87f8-e71fc4d1542f.JPG)
    
* Camera Screen:
    
  ![tempsnip](https://user-images.githubusercontent.com/34962951/122668191-90b07280-d1e9-11eb-823b-c7a29532ac3e.png)

* Final Result:
  ![final](https://user-images.githubusercontent.com/34962951/122667770-239bdd80-d1e7-11eb-965e-2cb8a1ccc46f.JPG)



* Demo video:

  Unfortunately, it takes a really long time for the api to processed the data, so I cut the videos
    
    


  * Testing Chinese text with file chooser:
  
    https://user-images.githubusercontent.com/34962951/122668527-0c5eef00-d1eb-11eb-8df5-32688ece6295.mp4

  * Testing Spanish text with file chooser:
    
    https://user-images.githubusercontent.com/34962951/122669100-4da4ce00-d1ee-11eb-9ebe-cd6a1a9e4a9b.mp4

  * Testing English text with camera:
  
    


## Reference
 1. [IBM Watsons Service](https://cloud.ibm.com/apidocs/text-to-speech)
    
 2. [OCR.space Free OCR API](https://ocr.space/OCRAPI)

 3. Testing Image :
    * https://wkee.net/post/studying-high-definition-maps-to-help-historical-research-ji-yang-s-comments-on-chen-jing-s-arti.html
    * https://www.ettoday.net/news/20160214/622569.htm
    * https://www.niemanlab.org/2016/02/en-espanol-the-new-york-times-launches-a-spanish-language-news-site-aiming-south-of-the-border/