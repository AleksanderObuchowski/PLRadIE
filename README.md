# Information Extraction From Polish Radiological Reports using language models
Radiology reports are vital elements of directing patient care. They are usually delivered in free text form, which makes them prone to errors, such as omission in reporting radiological findings and using difficult-to-comprehend mental shortcuts. Although structured reporting is the recommended method, its adoption continues to be limited. Radiologists find structured reports too limiting and burdensome. In this paper, we propose the model, which is meant to preserve the benefits of free text, while moving towards a structured report. The model automatically parametrizes Polish radiology reports based on language models. The models were trained on a large dataset of 1200 chest computed tomography (CT) reports annotated by multiple medical experts reports with 44 observation tags. Experimental analysis shows that models based on language models are able to achieve satisfactory results despite being pre-trained on general domain corpora. Overall, the model achieves an F1 score of 81 % and is able to successfully parametrize the most common radiological observations, allowing for potential adaptation in clinical practice. Our model is publically available.
<img width="719" alt="image" src="https://github.com/AleksanderObuchowski/PLRadIE/assets/12778421/460aab64-3028-4de1-b6d1-a93c13227c68">
# Paper
https://aclanthology.org/2023.bsnlp-1.14/
# Usage
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
Download model from https://www.sendbig.com/en/view-files/?Id=d5f7c43d-4ec4-39ed-c908-c4afed5eb091

Unzip the model to `saved_model` directory

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
```json
[[{'Serce': 'B-POWIĘKSZENIE_SERCA'}, {'powiększone,': 'I-POWIĘKSZENIE_SERCA'}, {'niewielka': 'B-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'ilość': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'płynu': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'w': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'worku': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}, {'osierdziowym': 'I-PŁYN_W_WORKU_OSIERDZIOWYM'}]]
```

See `example.py`

## Cite
```
@inproceedings{obuchowski-etal-2023-information,
    title = "Information Extraction from {P}olish Radiology Reports Using Language Models",
    author = "Obuchowski, Aleksander  and
      Klaudel, Barbara  and
      Jasik, Patryk",
    booktitle = "Proceedings of the 9th Workshop on Slavic Natural Language Processing 2023 (SlavicNLP 2023)",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.bsnlp-1.14",
    doi = "10.18653/v1/2023.bsnlp-1.14",
    pages = "113--122",
    abstract = "Radiology reports are vital elements of directing patient care. They are usually delivered in free text form, which makes them prone to errors, such as omission in reporting radiological findings and using difficult-to-comprehend mental shortcuts. Although structured reporting is the recommended method, its adoption continues to be limited. Radiologists find structured reports too limiting and burdensome. In this paper, we propose the model, which is meant to preserve the benefits of free text, while moving towards a structured report. The model automatically parametrizes Polish radiology reports based on language models. The models were trained on a large dataset of 1200 chest computed tomography (CT) reports annotated by multiple medical experts reports with 44 observation tags. Experimental analysis shows that models based on language models are able to achieve satisfactory results despite being pre-trained on general domain corpora. Overall, the model achieves an F1 score of 81{\%} and is able to successfully parametrize the most common radiological observations, allowing for potential adaptation in clinical practice. Our model is publically available.",
}
```
