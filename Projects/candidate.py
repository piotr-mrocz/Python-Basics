experience = 2

laguages = [
    "python",
    "typescript",
    "javascript",
    "java"
]

contractType = "b2b"

candidateExperiance = int(input("Experiance: "))
candidateLanguage = input("Language: ")

if (candidateExperiance >= experience and candidateLanguage in laguages):
    if contractType == "b2b" or contractType == "employment":
        print("You are accepted for work")
    else:
        print("Application rejected")
else:
    print("Application rejected. You don't have required experience")