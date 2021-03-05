class InitCookies:

    def __init__(self):
        self.csrftoken = 'g'
        self.mid = 'g'
        self.ig_did = 'g'
        self.ds_user_id = 'g'
        self.sessionid = 'g'
        self.ig_nrcb = 'g'
        self.rur = 'g'

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def get_dict(self):
        return self.__dict__

    def check_init_attributes(self):
        return True if all(self.get_dict().values()) else False


if __name__ == "__main__":
    cookies = InitCookies()
    print(cookies.check_init_attributes())
