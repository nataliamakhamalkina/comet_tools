# comet_tools

Scripts for COMET evaluation. 

# Dependencies
```python3 -m pip install xlsxwriter```

# Getting a scored table

```export_scores_to_excelwriter.py```

If given only one translation and one score file, creates a simple scored table:
|  src | translation |  score | reference |
|:----:|:-----------:|:------:|:---------:|
| Test | Текст       | 0.3678 | Тест      |

If given two translation files and two score files, creates a differetiated table:
|  src | translation1 | score1 | translation2 | score2 | reference | score2-score1 |
|:----:|:------------:|:------:|:------------:|:------:|:---------:|---------------|
| Test | Текст        | 0.3678 | Тесты        | 0.6456 | Тест      | 0,2778        |

To sort the translations by the score difference, open the .xlsx file and click the filter -> _Sort_ (Excel sorts values on runtime).

# COMET-DA usage
Use this notebook: [COMET-DA_pipeline.ipynb]().

# COMET-MQM usage
Use this notebook: [Comet-MQM pipeline.ipynb](https://colab.research.google.com/drive/15AmOsMPxcyhpSjq3xbB58GAdQolfPGKF#scrollTo=lyk2ag-o3--o).
