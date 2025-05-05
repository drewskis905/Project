class Map:
    """class handling our map
    attributes:
    def __new__ = creating an instance for our map
    def __init__ = initializing our map and stores our file content
    def __getitem__ = returns specific row for map
    def __len__ = returns number of rows in our map 
    def reveal = returns specific location
    def remove_at_loc = overwrites the character with n"""
    _instance = None
    _initialized = False 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Map._initialized:
            self._file = open("map_lab10.txt")
            self._map_content = []
            for row in self._file: #stores the file content in self._map_content
                list = []
                for item in row:
                    if item != ' ' or item != '\n':
                        list.append(item)
                self._map_content.append(list)
            self._revealed_list = []
            for row in self._map_content: #stores all False value 
                list = []
                for item in row:
                    list.append(False)
                self._revealed_list.append(list)
            self._file.close()
            Map._initialized = True

    def __getitem__(self, row): # returns the specific row from the map
        return self._map_content[row]
    
    def __len__(self): # returns the number of rows in the map list
        return len(self._map_content)
    
    def show_map(self, loc): #returns the map as a string with player, the map content, and the letter x at loc
        map_str = ""
        for row in range(len(self._map_content)):
            for col in range(len(self._map_content)):
                if [row,col] == loc:
                    map_str += '* '
                elif self._revealed_list[row][col]:
                    map_str += self._map_content[row][col] + " "
                else:
                    map_str += 'x '
            map_str += '\n'
        return map_str
    
    def reveal(self, loc): #turns the specific location in the self._revealed_list to True
        for row in range(len(self._map_content)):
            for col in range(len(self._map_content)):
                if [row,col] == loc:
                    self._revealed_list[row][col] = True

    def remove_at_loc(self, loc): #overwrites the character in the map list at the specific location with an 'n'
        for row in range(len(self._map_content)):
            for col in range(len(self._map_content)):
                if [row,col] == loc:
                    self._map_content[row][col] = 'n'
                    
    


            