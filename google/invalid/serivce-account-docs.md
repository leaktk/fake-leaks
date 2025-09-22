# Send metadata to Google Cloud

1. First create a service account (the credentials will look like this):
   ```json
   {
     "type": "service_account",
     "project_id": "<gcp-project-id>",
     "private_key_id": "55e82e1eb131597ce6ef77ff775b2c2e5f4d6b45",
     "private_key": "-----BEGIN PRIVATE KEY-----\n ... \n-----END PRIVATE KEY-----\n",
     "client_email": "prod-serviceaccount@coreapp-gce-prod.iam.gserviceaccount.com",
     "client_id": "<client-id>",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/prod-serviceaccount%40coreapp-gce-prod.iam.gserviceaccount.com"
   }
   ```
2. Save the account in the OCP secret
3. Configure the app to reference the secret
