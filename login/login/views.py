
def home(request):
    return render(request, 'home.html', {'what':'Django File Upload'})
 
def upload(request):

    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename):

    if not os.path.exists('files/'):
        os.mkdir('files/')
 
    with open('files/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)