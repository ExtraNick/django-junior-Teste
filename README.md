# Requisitos desafio 
## Django Júnior

Este é um desafio proposto pela SOIRTEC para ajudar na avaliação dos candidatos à vaga de desenvolvedor júnior.



Este projeto é baseado em "Escrevendo seu primeiro app Django" (https://docs.djangoproject.com/pt-br/5.1/intro/tutorial01/)

O objetivo deste desafio é entender o nível de conhecimento dos candidatos em desvios condicionais e laços simples.


### Desafio

 - Faça um fork(ou baixe o zip) deste projeto.
 - Siga o tutorial do django para criar o banco de dados, as tabelas, o usuário administrador e alguns registros de Questões e Respostas no banco de dados(pode utilizar o admin ou o shell do django, o que preferir).
 - Edite o arquivo polls/models.py para que o método total_votes retorne o total de votos que a Questão possui.
 - Edite novamente o arquivo polls/models.py para que o método has_votes retorne Verdadeiro caso a Questão possua respostas com votos ou Falso caso contrário.
 - Edite o .gitignore para incluir seu arquivo db.sqlite3 no projeto.

 Assim que estiver concluído, nos envie o link público do seu projeto no git(ou o zip, caso tenha dificuldades com o GIT) contendo, além do código, alguns prints da tela /polls/<id>/results/ mostrando os dados que foram incluidos nessa tela com as edições para o email desafio.dev@soirtec.com. (Não precisa editar o template, assim que os métodos estiverem funcionando, as informações irão aparecer na tela).

# Resultados desafio

Os arquivos aqui presentes representam o tutorial Django até a parte 4 + os desafios. <br>
- "Edite o arquivo polls/models.py para que o método total_votes retorne o total de votos que a Questão possui." <br>
Código:
```
    def total_votes(self): 
        return Choice.objects.aggregate(Sum('votes'))
```
incluido no Model "Question".<br>
- "Edite novamente o arquivo polls/models.py para que o método has_votes retorne Verdadeiro caso a Questão possua respostas com votos ou Falso caso contrário." <br>
Código:
```
    def has_votes(self): 
        check_status = Question.objects.filter(choice__votes__isnull=False)
        if str(check_status) == "<QuerySet []>": #TO-DO: realizar essa comparacao sem o matching de string. I.E: If Query Null 
            return False
        else: 
            return True
```
Exemplos de códigos acima em ação: <br>
![image](https://github.com/user-attachments/assets/9a8fd5ae-386f-4796-adf0-a8aa3af06846)

- "alguns prints da tela /polls/<id>/results/" <br> <br>

Screenshots: <br>
![image](https://github.com/user-attachments/assets/2a8ce710-e7f2-415c-b02e-62a52a6c09d9) <br>
pagina da Question "What's up?" <br> <br>
![image](https://github.com/user-attachments/assets/953780e5-147a-466f-9521-60495f417bb3) <br>
pagina voto Choice "Not much" <br> <br>
![image](https://github.com/user-attachments/assets/908c3f4c-964f-47a6-93ea-1afd6487a123) <br>
pagina voto Choice "The Sky" <br> <br>
![image](https://github.com/user-attachments/assets/f068658e-3909-48b5-861d-ac55b7e6eaa3) <br>
pagina voto Choice "Testando votes" <br> <br>
![image](https://github.com/user-attachments/assets/3e573c37-5bd3-4f80-a5b0-4252b86c3fb5) <br>
pagina voto Choice "Testando votes 2" <br> <br>
![image](https://github.com/user-attachments/assets/eb815e9c-48ba-4001-be9f-6646b1a73c8a) <br>
Total de votos pós demonstração de pagina votes <br> <br>
![image](https://github.com/user-attachments/assets/835c0358-e5be-454b-9999-965107559620) <br>
Pagina tratamento de error "Nenhum voto selecionado" <br> <br>






