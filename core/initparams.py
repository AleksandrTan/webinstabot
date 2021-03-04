class InitParams:

    def __init__(self, account_data: dict, initialization_parameters: dict):
        # if initialization_parameters are passed to the bot constructor
        if initialization_parameters:
            self.csrftoken = initialization_parameters["csrftoken"]
            self.mid = initialization_parameters["mid"]
            self.ig_did = initialization_parameters["id_did"]
            self.ds_user_id = initialization_parameters["ds_user_id"]
            self.sessionid = initialization_parameters["sessionid"]
            self.ig_nrcb = initialization_parameters["ig_nrcb"]
            self.rur = initialization_parameters["rur"]
        else:
            self.csrftoken = ''
            self.mid = ''
            self.ig_did = ''
            self.ds_user_id = ''
            self.sessionid = ''
            self.ig_nrcb = ''
            self.rur = ''
        self.account_data = account_data
        self.username = self.account_data["username"]
        self.password = self.account_data["password"]
        self.enc_password = ''

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def get_dict(self):
        return self.__dict__
