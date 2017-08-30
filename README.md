# CommuniData project
Public repository of the research project CommuniData: Open Data for Local Communities http://www.communidata.at

## Open Data in Austria

### Wordclouds
* titles from all 2297 datasets in data_gv_at portal, 373 datasets in www_opendataportal_at portal (latest snapshot: 1st week of 2017 '1701')
* Exception from the API: {u'message': u'QueuePool limit of size 20 overflow 10 reached, connection timed out, timeout 30'} after ~150 requests (data_gv_at: 1643 snapshot)

#### data.gv.at Wordcloud (2297 datasets as of 31.12.2016)
![data.gv.at wordcloud](results/data_gv_at_1701.png)

#### opendataportal.at Wordcloud (373 datasets as of 31.12.2016)
![opendataportal.at wordcloud](results/www_opendataportal_at_1701.png)

### Jupyter Notebook Tutorials

The tutorials are published on [our web-site](http://www.communidata.at)
<!-- or [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/vendi12/communidata) -->


## Search

* load csv files with get_portal_datasets.py script
* grep $PATTERN \*

For example, the following queries return the rows associated with the 2nd district of Vienna:
			 grep ";1020;" *
			 grep ";90200;" *
			 grep -i ";Leopoldstadt;" *

### ES search API sample results

Request: "Musik im Park"

Results: 
Garagen und Park & Ride-Anlagen - Standorte - Wien
Park- und Ride Anlagen K\xe4rnten
Musik- und Singschulen - Standorte - Wien


## StuwerNews

Tracking news for the local communities from social media (Twitter)

See https://github.com/vendi12/StuwerNews

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
* Sebastian Neumaier: [Open Data Portal Watch API](http://data.wu.ac.at/portalwatch/)

## References

### Open Data projects

* [ADEQUATe](https://www.adequate.at)

* Los Angeles City

** [Open Data portal](https://data.lacity.org/A-Livable-and-Sustainable-City/LASAN-Miles-of-Sewer-Cleaned/iyyp-p2fx)

** [GeoHub platform](http://geohub.lacity.org) + [Video](https://www.youtube.com/watch?v=iuUShx8hsWQ)

* [Durham Open Data](https://opendurham.nc.gov/page/reuse/) (OpenDataSoft)

* [Harvard Open Data](http://harvard-open-data-project.github.io)

* [Kaggle](https://www.kaggle.com/datasets)

### Jupyter Notebooks

* [tmpnb](https://github.com/jupyter/tmpnb)

... launches a docker container for each user that requests one.

... deploying via nginx.

* [JupyterHub Server](https://github.com/jupyterhub/jupyterhub)

[Deploying JupyterHub for Education](https://developer.rackspace.com/blog/deploying-jupyterhub-for-education/)

* [Declarative Widgets](https://github.com/jupyter/declarativewidgets) and [Dynamic Dashboards](https://github.com/jupyter/dashboards)

** [Tutorials](http://jupyter.cloudet.xyz)

** Health Inspection Dashboard Tutorial: [[Video]](https://www.youtube.com/watch?v=V3VxQGevHCU) [[Code]](https://github.com/jupyter-resources/tutorial-dashboards-declarativewidgets)

* [ipywidgets](https://github.com/ipython/ipywidgets)


* Plotly

* PivotTable.js

* [Lightning Server API](http://lightning-viz.org)
