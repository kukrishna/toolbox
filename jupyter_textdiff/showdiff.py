import difflib
import nltk

def showdiff(fr, to):
    differ = difflib.Differ()
    html=""

    for entry in differ.compare(nltk.sent_tokenize(fr), nltk.sent_tokenize(to)):
        if entry[0]=="+":
            html+="<tt style='white-space: pre;background-color:lightgreen'>"+entry+"</tt><br>"
        elif entry[0]=="-":
            html+="<tt style='white-space: pre;background-color:lightcoral'>"+entry+"</tt><br>"
        else:
            html+="<tt style='white-space: pre;'>"+entry+"</tt><br>"

    return html