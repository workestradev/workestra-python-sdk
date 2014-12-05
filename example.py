from workestra.workestraSDK import WorkestraSDK


#Create a new instance of the SDK
sdk = WorkestraSDK()

#Set your Api key
sdk.setApiKey('{Your-API-Key}')

#or use basic authentication
sdk.setBasicAuth('{Email}','{Password}')


#list the latest notification
print sdk.listNotifications()