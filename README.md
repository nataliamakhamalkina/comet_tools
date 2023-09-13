# comet_tools

Scripts for COMET evaluation. 

# Dependencies

```python3 -m pip install xlsxwriter```

# Getting a scored table

There are two ways to get scored tables.

1. Simple scored table

Give only one translation and one score file:

```python3 export_scores_to_excelwriter.py source reference translation scores outfile```

Output example:

|  src | translation |  score | reference |
|:----:|:-----------:|:------:|:---------:|
| Test | Текст       | 0.3678 | Тест      |

2. Differentiated table

Give two translation files and two score files:

```python3 export_scores_to_excelwriter.py source reference translation1 scores1 translation2 scores2 outfile```

Output example:

|  src | translation1 | score1 | translation2 | score2 | reference | score2-score1 |
|:----:|:------------:|:------:|:------------:|:------:|:---------:|---------------|
| Test | Текст        | 0.3678 | Тесты        | 0.6456 | Тест      | 0,2778        |

To sort the translations by the score difference, open the .xlsx file and click the filter -> _Sort_ (Excel sorts values on runtime).

# COMET-DA usage

Use this notebook: [COMET-DA_pipeline.ipynb]().

# COMET-MQM usage

Use this notebook: [Comet-MQM pipeline.ipynb](https://colab.research.google.com/drive/15AmOsMPxcyhpSjq3xbB58GAdQolfPGKF#scrollTo=lyk2ag-o3--o).
