class InitParams:

    def __init__(self, initialization_parameters: dict = None):
        self.fetch_media_item_cursor = ''
        self.has_next_page = True
        self.posts_id_list = list()
        # if initialization_parameters are passed to the bot constructor
        if initialization_parameters:
            for param in initialization_parameters.items():
                self.__setattr__(param[0], param[1])

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def get_dict(self):
        return self.__dict__
