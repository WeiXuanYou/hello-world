class Query:
    def __init__(self, client, name):
        self.client = client
        self.parameters = {"name": name}
        self.command = "query"

    def execute(self):
        self.client.send_command(
            self.command, self.parameters)
        resive_data = self.client.wait_response()

        return resive_data
