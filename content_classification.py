import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


file = open("twitter.txt")
 
while 1:
    text = file.readline()
    text*=100
    if not text:
        break
    pass 

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
      text = text.decode('utf-8')

    document = types.Document(
      content=text.encode('utf-8'),
      type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))