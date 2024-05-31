# Currency-app
This is a streamlit app developed for the "Tooling for data scientist" course for X-HEC DSB 2024.
It is based on a Kaggle dataset and shows the exchange rate of a chosen currency vis-a-vis the euro. 

The dataset can be found and downloaded here : https://www.kaggle.com/datasets/lsind18/euro-exchange-daily-rates-19992020/code?resource=download

I recommend creating a "Dataset" folder and storing the csv file there to run the app.

## Docker
The app has been contenairized on docker and its image is available at this link : https://hub.docker.com/r/adherouville/currency-exchange-rate-app

It can be run with the following commands : 
'docker pull adherouville/currency-exchange-rate-app'
and :
'run -d --name currency-exchange-app -p 8080:8501 adherouville/currency-exchange-rate-app:latest'

