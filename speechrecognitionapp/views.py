import json
from django.http import JsonResponse
from django.shortcuts import render
import googletrans
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def translate_text(request):
    if request.method == 'POST':
        try:
            final = json.loads(request.body.decode('utf-8'))

            # Extract the recognized text from the POST request
            data = final.get('text','')
            # print("here is output",data)
            lang = final.get('trans','')
            print("language:  ",lang)
            # Perform translation (using googletrans for example)
            translator = googletrans.Translator()
            translated_text = translator.translate(data, src='auto', dest=lang)  # Translate from English to Spanish
            # You can change 'es' to the desired target language code

            # Return the translated text as JSON response
            return JsonResponse({'translated_text': translated_text.text})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})


def index(request):
    return render(request, 'index.html')

