workestra-python-sdk
==========

A Python SDK library for the [Workestra API](https://www.workestra.co/developers/docs)


To use the library, you'll need to install the request package as follow :

pip install -r requirements.txt


You will need an API key to get started. You can find instructions on obtaining an API key [here](https://www.workestra.co/developers/docs#authentication)

Once you have that, the following code will get the latest notifications (as long as your user is able to access those notifications)

````

from workestra.workestraSDK import WorkestraSDK


#Create a new instance of the SDK
sdk = WorkestraSDK()

#Set your Api key
sdk.setApiKey('{Your-API-Key}')

#or use basic authentication
sdk.setBasicAuth('{Email}','{Password}')


#list the latest notification
print sdk.listNotifications()


````

After that, you may want to explore the stream [api](https://www.workestra.co/developers/docs#sream), or just look through the wrapper code.

