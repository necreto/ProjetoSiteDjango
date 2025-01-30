from django.shortcuts import render, redirect
from django.contrib import messages  
from django.shortcuts import get_object_or_404
from base.utils import add_form_errors_to_messages
from forum.forms import PostagemForumForm
from forum import models

# Lista de Postagem
def lista_postagem_forum(request):
	postagens = models.PostagemForum.objects.filter(ativo=True)
	context = {'postagens': postagens}
	return render(request, 'lista-postagem-forum.html', context)

# Cria postagens 
def criar_postagem_forum(request):
    form = PostagemForumForm()
    if request.method == 'POST':
        form = PostagemForumForm(request.POST, request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.usuario = request.user
            forum.save()
            # Redirecionar para uma página de sucesso ou fazer qualquer outra ação desejada
            messages.success(request, 'Seu Post foi cadastrado com sucesso!')
            return redirect('lista-postagem-forum')
        else:
            add_form_errors_to_messages(request, form)
            
    return render(request, 'form-postagem-forum.html', {'form': form})

# Detalhe das postagem (ID)
def detalhe_postagem_forum(request, id):
    postagem = get_object_or_404(models.PostagemForum, id=id)
    return render(request, 'detalhe-postagem-forum.html', {'postagem': postagem})