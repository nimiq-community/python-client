class SessionStub():
    testData = None
    latestRequest = None
    latestRequestMethod = None
    latestRequestParams = None

    def post(self, url, json, auth):
        SessionStub.latestRequest = json
        SessionStub.latestRequestMethod = json.get("method")
        SessionStub.latestRequestParams = json.get("params")[0]
        return self

    def json(self):
        return SessionStub.testData
