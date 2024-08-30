# FActScore

## Install
<!-- ```
conda create -n fs-env python=3.9
conda activate fs-env
pip install -r requirements.txt
``` -->

Make a new Python 3.7+ environment using `virtualenv` or `conda`.

```bash
pip install --upgrade factscore
python -m spacy download en_core_web_sm
```

## Download the data

```bash
python -m factscore.download_data
```

## Usage

See `example.ipynb`.
