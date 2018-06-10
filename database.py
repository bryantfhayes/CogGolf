import json, os

#
# Abstract Database class
#
class Database(object):
    def __init__(self):
        pass

    def getObjectForPath(self, path):
        ''' Given a '/' seperated path, return value of None is nothing is there '''
        pass

    def setObjectForPath(self, path, value):
        ''' Given a '/' seperated path, set a value at that path. Path will be created if it does not exist '''
        pass

    def reloadDatabase(self):
        ''' Reload database from source '''
        pass

    def saveDatabase(self):
        ''' Explicilty write database to disk '''
        pass

#
# A Simple File Database which stores data as a JSON file on disk
#
class SFDatabase(Database):
    def __init__(self, path):
        Database.__init__(self)
        self.path = path
        self.data = {}
        self.reloadDatabase()

    def getObjectForPath(self, path):
        cursor = self.data
        items = path.split('/')
        for item in items:
            if item in cursor:
                cursor = cursor[item]
                continue
            return None
        return cursor

    def _setObjectForPath(self, items, value, cursor):
        #print("_setObjectForPath", items, value, self.data, cursor)
        #print("")
        if len(items) == 0:
            return
        elif len(items) == 1:
            cursor[items[0]] = value
            return
        else:
            if items[0] not in cursor:
                cursor[items[0]] = {}

            # Make sure item is dictionary, and not an endpoint
            if not isinstance(cursor[items[0]], dict):
                cursor[items[0]] = {}

            self._setObjectForPath(items[1:], value, cursor[items[0]])

    def setObjectForPath(self, path, value):
        items = path.split('/')
        self._setObjectForPath(items, value, self.data)
        self.saveDatabase()

    def reloadDatabase(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r') as fp:
                self.data = json.load(fp)
        else:
            self.saveDatabase()

    def saveDatabase(self):
        with open(self.path, 'w') as fp:
            json.dump(self.data, fp)


if __name__ == "__main__":
    sf = SFDatabase("test.json")
    sf.setObjectForPath("test", "Empty!")
    print(sf.getObjectForPath("test"))
    
    sf.setObjectForPath("test/item1/item2/item3", "deep!")
    print(sf.getObjectForPath("test"))

    sf.setObjectForPath("test", "Empty!")
    print(sf.getObjectForPath("test"))

    sf.setObjectForPath("test/item1", "Item1")
    print(sf.getObjectForPath("test"))

    sf.setObjectForPath("test/item1", {"Item1Dict" : "test!"})
    print(sf.getObjectForPath("test"))

    sf.setObjectForPath("test/item1/Item2Dict", "Another test")
    print(sf.getObjectForPath("test"))

    sf.setObjectForPath("test/item1/Item2Dict", "EDIT: Another test")
    print(sf.getObjectForPath("test"))
