from django.shortcuts import render, HttpResponse


def quiz(request):
    currentquizno = 0
    # currentquizno+=1
    true = True
    false = False

    return render(request, "question.html", {"q": currentquizno, "btn": true, "bt": false})


def test(request):
    name = "Rahul Dravid"
    profession = "coach"
    return render(request, "test.html", {"name": name, "key1": profession})


#
#

def showtoconsol(request):
    name = "rahul dravid"
    profession = "coach"
    print(name)
    print("name")
    profession = "mahabharat"
    return render(request, "textfield.html", {"data": name, "object": profession})


"""
def question(request):
    questions=["where is lanka","where is tokyo","where is Madiyahu","where is daanganj","where is africa"]
    # currentquestion=0
    x = 0
    n=len(questions)
    if request.GET:
        x=request.GET["question"]
        x=int(x)
        x=x+1
        print('x',x)
        if x>=n:
            print("test over")
        return HttpResponse("test over")
    question=questions[x]
    """

# return render(request,"question.html",{"qno":x,"currentquestion":question})
""


def question(request):
    questions = [('(1)- Python was developed by Guido van Rossum', 1),
                 ('(2)- python is a case sensitive language', 1),
                 ('(3)- Python is object-oriented language', 1),
                 ('(4)- C++ is not a programming language', 0),
                 ('(5)- C++ is oops concepts--', 1),
                 ('(6)- Python is a scripting language', 1),
                 ('(7)- Python is a programming language', 1),
                 ('(8)- Python is a open source language', 1),
                 ('(9)- Python support print() statement', 1),
                 ('(10)-Python is a compiled language', 0)]

    correctresult='<span class="material-icons" style="color: green">check</span>'
    wrongresult='<span class="material-icons" style="color: red">close</span>'

    x = 0
    previousquestion = ""
    result = ""
    option = ""
    score = 0

    n = len(questions)
    if request.GET:
        x = request.GET["question"]
        option = int(request.GET["option"])
        score = request.GET["score"]
        x = int(x)
        score = int(score)
        previousans = questions[x][1]
        previousquestion = questions[x][0]
        if option == previousans:
            result = "Correct"
            score = score + 1
        else:
            result = "Wrong"
        x = x + 1
        print(result,"option", option,"answer", previousans)
        if x >= n:
            return HttpResponse("Test-Over -- Your Scores is  ---" + str(score))


    question = questions[x][0]
    return render(request, "check.html",
                  {"qno": x, "currentquestion": question, "result": result, "previousans": previousquestion,
                   "score": score})

