from django.shortcuts import render
from django.shortcuts import redirect
from .models import Todo
from django.views.generic import UpdateView

from django.views.generic.edit import UpdateView
# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        color = request.POST.get("color")
        res = Todo.objects.create(title=title,text=text,color=color,)
        res.save()
    context = {"todos":Todo.objects.all(),"count":len(Todo.objects.all()),"done":len(Todo.objects.filter(done=True))}
    return render(request,'index.html',context)

def deleteTodo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("/")

def deleteAll(reuest):
    todo = Todo.objects.all()
    todo.delete()
    return redirect("/")

def done_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = True
    todo.save()
    return redirect("/")
def udpade(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = False
    todo.save()
    return redirect("/")

class UpdateTodo(UpdateView):
    model = Todo
    fields = ['title','text','color']
    template_name = 'index.html'
    success_url = '/'