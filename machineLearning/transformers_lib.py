from transformers import pipeline

translator = pipeline("translation_en_to_de")
print(("My name is Amit and I love learning!"))
print("In German:")
print(translator("My name is Amit and I love learning!"))


