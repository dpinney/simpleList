import dropbox
from dropbox.datastore import DatastoreManager
from dropbox.client import DropboxClient, DropboxOAuth2FlowNoRedirect

APP_KEY = "TBD"
APP_SECRET = "TBD"
# From getAuthKey:
ACC_TOKEN = "TBD"
UID = 6925109

def getAuthKey():
	# Have the user sign in and authorize this token
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()
	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()
	access_token, user_id = flow.finish(code)
	print "Access token:", access_token
	print "User ID:", user_id

def testConnection():
	# Simple test of an access token.
	client = DropboxClient(ACC_TOKEN)
	print 'linked account: ', client.account_info()

def createTable():
	# Make a simple table.
	client = DropboxClient(ACC_TOKEN)
	manager = DatastoreManager(client)
	datastore = manager.open_default_datastore()
	tasks_table = datastore.get_table('tasks')
	first_task = tasks_table.insert(taskname='Buy milk', completed=False)
	datastore.commit()
	tasks = tasks_table.query(completed=False)
	for task in tasks:
		print task.get('taskname')

def queryStore():
	# Query tasks table.
	client = DropboxClient(ACC_TOKEN)
	manager = DatastoreManager(client)
	datastore = manager.open_default_datastore()
	tasks_table = datastore.get_table('tasks')
	tasks = tasks_table.query(completed=False)
	for task in tasks:
		print task

if __name__ == '__main__':
	queryStore()