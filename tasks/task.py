class HistoryDict:
    def __init__(self, init_dict={}) -> None:
        self.main_dictionary = init_dict
        self.history_list = []

    def set_value(self, key, value):
        self.main_dictionary.update({key:value})
        if len(self.history_list) < 5:
            self.history_list.append(key)
        else:
            del self.history_list[0]
            self.history_list.append(key)
    

    def get_history(self):
        return self.history_list


if __name__=="__main__":
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.set_value("4u4a", 90)
    print(d.get_history())
    #committing to GitHub