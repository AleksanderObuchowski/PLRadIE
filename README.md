# Information Extraction From Polish Radiological Reports using language models

## Requirements
This reposetory was created using `python 3.8.10`
### Simple start
```bash
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

```
### Install packages yourself

* **Pytorch**

    https://pytorch.org/get-started/locally/
* **Simple Transformers**

    Use this version as the main project doesn't support LUKE models yet
    https://github.com/whr778/simpletransformers/tree/add-luke-mluke-to-ner

## Usage
```python
from simpletransformers.ner import NERModel, NERArgs


model = NERModel(
    "mluke",
    "saved_model",
)

prediction, raw_outputs = model.predict(["Serce powiększone, niewielka ilość płynu w worku osierdziowym"])
print(prediction)
```
Output:
```
[[{'Serce': 'B-POWIĘKSZENIE_SERCA'}, {'powiększone,': 'I-POWIĘKSZENIE_SERCA'}, {'niewielka': 'B-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'ilość': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'płynu': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'w': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'worku': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'osierdziowym': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}]]
```

See `example.py`