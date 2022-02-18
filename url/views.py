from django.shortcuts import redirect, render
import pyshorteners

def url_shortner(request):
  if request.method == 'POST':
      long_url = request.POST['url']
      pys = pyshorteners.Shortener()
      short_url = pys.tinyurl.short(long_url)
      return render(request,'url/urlShortner.html', context={'short_url':short_url,'long_url':long_url})
  else:
      return render(request,'url/urlShortner.html')