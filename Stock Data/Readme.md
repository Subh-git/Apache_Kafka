### Stock Data Analysis

1. These scripts are meant to be run to obtain the stock data from alphavantage api using the api key.

2. First we set up the server like zookeeper and kafka broker.

3. Then we execute the consumer script and then producer script to maintain the flow of data.

4. Then at last we stop the consumer scritp when we know that all data are executed and then finally we execute the hdfs script to copy the csv file to the hdfs.