from boto.connection import AWSAuthConnection

class ESConnection(AWSAuthConnection):

    def __init__(self, region, **kwargs):
        super(ESConnection, self).__init__(**kwargs)
        self._set_auth_region_name(region)
        self._set_auth_service_name("es")

    def _required_auth_capability(self):
        return ['hmac-v4']

if __name__ == "__main__":

    client = ESConnection(
            region='us-east-1',
            host='search-test-24hilpzr52vsxszl4ufgu46ura.us-east-1.es.amazonaws.com',
            aws_access_key_id='AKIAI6PHPAOUEXRIOXEQ',
            aws_secret_access_key='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', is_secure=False)

    print 'Registering Snapshot Repository'
    resp = client.make_request(method='POST',
            path='/_snapshot/backups',
            data='{"type": "s3","settings": { "bucket": "elasticdata2017","region": "us-east-1","role_arn": "arn:aws:iam::888111596762:role/test-elasticsearchRole"}}')
    body = resp.read()
    print body
