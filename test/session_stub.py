class SessionStub:
    test_data = None
    latest_request = None
    latest_request_method = None
    latest_request_params = None

    def post(self, url, json, auth):
        SessionStub.latest_request = json
        SessionStub.latest_request_method = json.get("method")
        SessionStub.latest_request_params = json.get("params")
        return self

    def json(self):
        return SessionStub.test_data
