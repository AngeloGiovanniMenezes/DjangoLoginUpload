from django.shortcuts import render

def requestLogout (pedido):

    logout(pedido)
    messages.info(pedido, "Deslogado com sucesso!")
    return redirect("main:homepage")
    