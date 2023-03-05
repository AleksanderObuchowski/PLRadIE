from simpletransformers.ner import NERModel, NERArgs


model = NERModel(
    "mluke",
    "saved_model",
)

prediction, raw_outputs = model.predict(["Serce powiększone, niewielka ilość płynu w worku osierdziowym"])
print(prediction)