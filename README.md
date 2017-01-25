# CommuniData project
Public repository of the research project CommuniData: Open Data for Local Communities http://www.communidata.at

## Open Data in Austria

* titles from all 2297 datasets in data_gv_at portal, 373 datasets in www_opendataportal_at portal (latest snapshot: 1st week of 2017 '1701')
* Exception from the API: {u'message': u'QueuePool limit of size 20 overflow 10 reached, connection timed out, timeout 30'} after ~150 requests (data_gv_at: 1643 snapshot)

#### data.gv.at Wordcloud (2297 datasets as of 31.12.2016)
![data.gv.at wordcloud](results/data_gv_at_1701.png)

#### opendataportal.at Wordcloud (373 datasets as of 31.12.2016)
![opendataportal.at wordcloud](results/www_opendataportal_at_1701.png)


## Search

* load csv files with get_portal_datasets.py script
* grep $PATTERN \*

For example, the following queries return the rows associated with the 2nd district of Vienna:
			 grep ";1020;" *
			 grep ";90200;" *
			 grep -i ";Leopoldstadt;" *

## Prerequisites
### Wordcloud
* [wordcloud](https://github.com/amueller/word_cloud)
* matplotlib
* Pillow

### Jupyter Notebooks
* pandas
* seaborn

## License

This project is licensed under the MIT License

## Acknowledgments

* Austrian Research Promotion Agency (FFG)
* Sebastian Neumaier: Open Data Portal Watch API http://data.wu.ac.at/portalwatch/

## References

### Open Data projects

* ADEQUATe project

https://www.adequate.at

* Los Angeles GeoHub

http://geohub.lacity.org

https://www.youtube.com/watch?v=iuUShx8hsWQ

* Los Angeles Open Data

https://data.lacity.org/A-Livable-and-Sustainable-City/LASAN-Miles-of-Sewer-Cleaned/iyyp-p2fx

* Harvard Open Data Project

http://harvard-open-data-project.github.io

* Kaggle

https://www.kaggle.com/datasets

### Jupyter Notebooks

* tmpnb

Sample server: http://jupyter.cloudet.xyz/user/IkdqW98Ie37B/notebooks/index.ipynb

* JupyterHub Server

https://github.com/jupyterhub/jupyterhub

* Dynamic Dashboards

* ipywidgets package

* Plotly

* PivotTable.js

* Declarative Widgets

* Lightning Server API

http://lightning-viz.org
