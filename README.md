# Berkeley Data Bootcamp: Project 4
> Neural Networks: Finding hidden relationships to make educated predictions

## Folder Contents
- A main `flask_app` folder containing all the website demonstration functionality
- A `.gitignore` file for Jupyter Notebook checkpoints and other commonly gitignored Python entities.

### Installation/Prerequisites
- Make sure you can run Python. The development environment we used was set-up with:
```
conda create -n dev python=3.10 anaconda -y
```
#### Imported Modules
- Installing via the conda command given should give you access to all of the script's modules locally. However, if you don't have them, be sure to grab yourself the following libraries:
  - [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) and [NumPy](https://numpy.org/install/) for basic data management and manipulation
  - [Scikit-Learn](https://scikit-learn.org/stable/install.html) for some clustering runs
  - [Flask](https://flask.palletsprojects.com/en/2.3.x/installation/) to handle frontend to backend communication
  - [SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html#installation) for basic Python-based SQL functionality
  - [Tensorflow](https://www.tensorflow.org/install) to program and run our neural networks
  - The other imports you may notice are native Python modules and should have come with your Python downloads, no links are necessary. Any errors on that end are dependent on the machine's Python installation and pathing process.
 
- Any dependencies we used are all pulled online from CDNs and official releases, but please refer to the links below if you want to examine the specific version used in this project or download the modules with NPM for work with Node.js:
  - [D3 v7](https://d3js.org/getting-started#d3-in-vanilla-html) to read JSON files and handle DOM tree element manipulation.
  - [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) to style our website.
 
Sources:
  - [IRS Tax Data](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi)
  - [ZIP to map coordinates conversion data](https://simplemaps.com/data/us-zips)
  - [CDC PLACES Data](https://chronicdata.cdc.gov/500-Cities-Places/PLACES-ZCTA-Data-GIS-Friendly-Format-2022-release/kee5-23sr)

## FINAL NOTES
> Project completed on October 2, 2023
