class NaLangInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def log(self, text):
        print(text)

    def log_error(self):
        print("LogError")
        
    def get_variable(self, var_name):
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            self.log_error()
            return None

    def set_variable(self, var_name, value):
        self.variables[var_name] = value

    def run(self, code):
        lines = code.split("\n")
        skip_next_line = False
        for line in lines:
            if skip_next_line:
                skip_next_line = False
                continue
            if line.strip(): 
                if line.strip().startswith("val "):
                    parts = line.strip().split(" ")
                    var_type = parts[1]
                    var_name = parts[2]
                    if var_type == "string":
                        self.variables[var_name] = ""
                    elif var_type == "integer":
                        self.variables[var_name] = 0
                    elif var_type == "float":
                        self.variables[var_name] = 0.0
                    elif var_type == "bool":
                        self.variables[var_name] = False
                    elif var_type == "list":
                        self.variables[var_name] = []
                    elif var_type == "map":
                        self.variables[var_name] = {}
                    elif var_type == "set":
                        self.variables[var_name] = set()
                    elif var_type == "dict":
                        self.variables[var_name] = dict()
                    elif var_type == "struct":
                        self.variables[var_name] = {}
                elif line.strip().startswith("valLog(") and line.strip().endswith(")"):
                    var_name = line.strip()[7:-1]
                    if var_name in self.variables:
                        print(self.variables[var_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("assign "):
                    parts = line.strip().split(" ")
                    var_name = parts[1]
                    var_value = parts[2][1:-1] 
                    if var_name in self.variables:
                        self.variables[var_name] = var_value
                    else:
                        self.log_error()
                elif line.strip().startswith("listAdd(") and line.strip().endswith(")"):
                    parts = line.strip()[8:-1].split(",")
                    list_name = parts[0]
                    item = parts[1][1:-1]  
                    if list_name in self.variables:
                        self.variables[list_name].append(item)
                    else:
                        self.log_error()
                elif line.strip().startswith("listRemove(") and line.strip().endswith(")"):
                    parts = line.strip()[11:-1].split(",")
                    list_name = parts[0]
                    item = parts[1][1:-1] 
                    if list_name in self.variables:
                        if item in self.variables[list_name]:
                            self.variables[list_name].remove(item)
                        else:
                            self.log_error()
                    else:
                        self.log_error()
                elif line.strip().startswith("listLog(") and line.strip().endswith(")"):
                    list_name = line.strip()[8:-1]
                    if list_name in self.variables:
                        print(self.variables[list_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("mapPut(") and line.strip().endswith(")"):
                    parts = line.strip()[7:-1].split(",")
                    map_name = parts[0]
                    key = parts[1][1:-1]
                    value = parts[2][1:-1] 
                    if map_name in self.variables:
                        self.variables[map_name][key] = value
                    else:
                        self.log_error()
                elif line.strip().startswith("mapRemove(") and line.strip().endswith(")"):
                    parts = line.strip()[10:-1].split(",")
                    map_name = parts[0]
                    key = parts[1][1:-1] 
                    if map_name in self.variables:
                        if key in self.variables[map_name]:
                            del self.variables[map_name][key]
                        else:
                            self.log_error()
                    else:
                        self.log_error()
                elif line.strip().startswith("mapLog(") and line.strip().endswith(")"):
                    map_name = line.strip()[7:-1]
                    if map_name in self.variables:
                        print(self.variables[map_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("setAdd(") and line.strip().endswith(")"):
                    parts = line.strip()[7:-1].split(",")
                    set_name = parts[0]
                    item = parts[1][1:-1] 
                    if set_name in self.variables:
                        self.variables[set_name].add(item)
                    else:
                        self.log_error()
                elif line.strip().startswith("setRemove(") and line.strip().endswith(")"):
                    parts = line.strip()[10:-1].split(",")
                    set_name = parts[0]
                    item = parts[1][1:-1] 
                    if set_name in self.variables:
                        if item in self.variables[set_name]:
                            self.variables[set_name].remove(item)
                        else:
                            self.log_error()
                    else:
                        self.log_error()
                elif line.strip().startswith("setLog(") and line.strip().endswith(")"):
                    set_name = line.strip()[7:-1]
                    if set_name in self.variables:
                        print(self.variables[set_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("strip(") and line.strip().endswith(")"):
                    parts = line.strip()[6:-1].split(",")
                    var_name = parts[0]
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].strip()
                    else:
                        self.log_error()
                elif line.strip().startswith("replace(") and line.strip().endswith(")"):
                    parts = line.strip()[8:-1].split(",")
                    var_name = parts[0]
                    old_value = parts[1][1:-1] 
                    new_value = parts[2][1:-1] 
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].replace(old_value, new_value)
                    else:
                        self.log_error()
                elif line.strip().startswith("split(") and line.strip().endswith(")"):
                    parts = line.strip()[6:-1].split(",")
                    var_name = parts[0]
                    delimiter = parts[1][1:-1] 
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].split(delimiter)
                    else:
                        self.log_error()
                elif line.strip().startswith("format(") and line.strip().endswith(")"):
                    parts = line.strip()[7:-1].split(",")
                    var_name = parts[0]
                    format_args = [part[1:-1] for part in parts[1:]]
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].format(*format_args)
                    else:
                        self.log_error()
                elif line.strip().startswith("join(") and line.strip().endswith(")"):
                    parts = line.strip()[5:-1].split(",")
                    var_name = parts[0]
                    delimiter = parts[1][1:-1] 
                    if var_name in self.variables:
                        self.variables[var_name] = delimiter.join(self.variables[var_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("swapcase(") and line.strip().endswith(")"):
                    var_name = line.strip()[9:-1]
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].swapcase()
                    else:
                        self.log_error()
                elif line.strip().startswith("lower(") and line.strip().endswith(")"):
                    var_name = line.strip()[6:-1]
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].lower()
                    else:
                        self.log_error()
                elif line.strip().startswith("upper(") and line.strip().endswith(")"):
                    var_name = line.strip()[6:-1]
                    if var_name in self.variables:
                        self.variables[var_name] = self.variables[var_name].upper()
                    else:
                        self.log_error()
                
                elif line.strip().startswith("sort(") and line.strip().endswith(")"):
                    list_name = line.strip()[5:-1]
                    if list_name in self.variables:
                        self.variables[list_name].sort()
                    else:
                        self.log_error()        
                        
                elif line.strip().startswith("dictPut(") and line.strip().endswith(")"):
                    parts = line.strip()[8:-1].split(",")
                    dict_name = parts[0]
                    key = parts[1][1:-1]  
                    value = parts[2][1:-1]  
                    if dict_name in self.variables:
                        self.variables[dict_name][key] = value
                    else:
                        self.log_error()
                elif line.strip().startswith("dictRemove(") and line.strip().endswith(")"):
                    parts = line.strip()[11:-1].split(",")
                    dict_name = parts[0]
                    key = parts[1][1:-1]  
                    if dict_name in self.variables:
                        if key in self.variables[dict_name]:
                            del self.variables[dict_name][key]
                        else:
                            self.log_error()
                    else:
                        self.log_error()
                elif line.strip().startswith("dictLog(") and line.strip().endswith(")"):
                    dict_name = line.strip()[8:-1]
                    if dict_name in self.variables:
                        print(self.variables[dict_name])
                    else:
                        self.log_error()
                elif line.strip().startswith("ListCreateWithType(") and line.strip().endswith(")"):
                    parts = line.strip()[18:-1].split(",")
                    var_name = parts[0]
                    var_type = parts[1]
                    if var_type == "string":
                        self.variables[var_name] = []
                    elif var_type == "integer":
                        self.variables[var_name] = []
                    elif var_type == "float":
                        self.variables[var_name] = []
                    elif var_type == "bool":
                        self.variables[var_name] = []
                    else:
                        self.log_error()
                elif line.strip().startswith("MapCreateWithType(") and line.strip().endswith(")"):
                    parts = line.strip()[17:-1].split(",")
                    var_name = parts[0]
                    var_type = parts[1]
                    if var_type == "string":
                        self.variables[var_name] = {}
                    elif var_type == "integer":
                        self.variables[var_name] = {}
                    elif var_type == "float":
                        self.variables[var_name] = {}
                    elif var_type == "bool":
                        self.variables[var_name] = {}
                    else:
                        self.log_error()
                elif line.strip().startswith("SetCreateWithType(") and line.strip().endswith(")"):
                    parts = line.strip()[17:-1].split(",")
                    var_name = parts[0]
                    var_type = parts[1]
                    if var_type == "string":
                        self.variables[var_name] = set()
                    elif var_type == "integer":
                        self.variables[var_name] = set()
                    elif var_type == "float":
                        self.variables[var_name] = set()
                    elif var_type == "bool":
                        self.variables[var_name] = set()
                    else:
                        self.log_error()
                elif line.strip().startswith("DictCreateWithType(") and line.strip().endswith(")"):
                    parts = line.strip()[18:-1].split(",")
                    var_name = parts[0]
                    var_type = parts[1]
                    if var_type == "string":
                        self.variables[var_name] = {}
                    elif var_type == "integer":
                        self.variables[var_name] = {}
                    elif var_type == "float":
                        self.variables[var_name] = {}
                    elif var_type == "bool":
                        self.variables[var_name] = {}
                    else:
                        self.log_error()
                        
                elif line.strip().startswith("listPop(") and line.strip().endswith(")"):
                    var_name = line.strip()[8:-1]
                    if var_name in self.variables and isinstance(self.variables[var_name], list):
                        if self.variables[var_name]:
                            popped_item = self.variables[var_name].pop()
                            print(f"{popped_item}")
                        else:
                            self.log_error("List is empty")
                    else:
                        self.log_error("Variable is not a list or does not exist")

                elif line.strip().startswith("StructCreate(") and line.strip().endswith(")"):
                    parts = line.strip()[13:-1].split(",")
                    struct_name = parts[0]
                    var1_type = parts[1]
                    var2_type = parts[2]
                    var3_type = parts[3]
                    var1_name = parts[4]
                    var2_name = parts[5]
                    var3_name = parts[6]
                    if var1_type in ["string", "integer", "float", "bool"] and \
                            var2_type in ["string", "integer", "float", "bool"] and \
                            var3_type in ["string", "integer", "float", "bool"]:
                        self.variables[struct_name] = {
                            var1_name: None,
                            var2_name: None,
                            var3_name: None
                        }
                    else:
                        self.log_error()

                elif line.strip().startswith("StructAssign(") and line.strip().endswith(")"):
                    parts = line.strip()[13:-1].split(",")
                    struct_name = parts[0]
                    var1_value = parts[1][1:-1]  
                    var2_value = parts[2][1:-1] 
                    var3_value = parts[3][1:-1]  
                    if struct_name in self.variables:
                        self.variables[struct_name] = {
                            var1_name: var1_value,
                            var2_name: var2_value,
                            var3_name: var3_value
                        }
                    else:
                        self.log_error()

                elif line.strip().startswith("StructLog(") and line.strip().endswith(")"):
                    struct_name = line.strip()[10:-1]
                    if struct_name in self.variables:
                        struct_data = self.variables[struct_name]
                        for key, value in struct_data.items():
                            print(key + "" + str(value))
                    else:
                        self.log_error()

                elif line.strip().startswith("structSet(") and line.strip().endswith(")"):
                    parts = line.strip()[10:-1].split(",")
                    struct_name = parts[0]
                    field_name = parts[1][1:-1]  
                    field_value = parts[2][1:-1]  
                    if struct_name in self.variables and isinstance(self.variables[struct_name], dict):
                        self.variables[struct_name][field_name] = field_value
                    else:
                        self.log_error()
                elif line.strip().startswith("structGet(") and line.strip().endswith(")"):
                    parts = line.strip()[10:-1].split(",")
                    struct_name = parts[0]
                    field_name = parts[1][1:-1]  
                    if struct_name in self.variables and isinstance(self.variables[struct_name], dict):
                        print(self.variables[struct_name].get(field_name, None))
                    else:
                        self.log_error()
                        
                elif line.strip().startswith("ptrGet(") and line.strip().endswith(")"):
                    var_name = line.strip()[7:-1]
                    value = self.get_variable(var_name)
                    if value is not None:
                        print(value)
                elif line.strip().startswith("ptrSet(") and line.strip().endswith(")"):
                    parts = line.strip()[7:-1].split(",")
                    var_name = parts[0]
                    value = parts[1][1:-1]  
                    self.set_variable(var_name, value)
                elif line.strip().startswith("try"):
                    try:
                    
                        self.variables = {}
                        skip_next_line = True
                    except:
                        self.log_error()
                elif line.strip().startswith("expect"):
                    if skip_next_line:
                        self.log("LogError")
                elif line.strip() == "pass":
                    pass
                
                
                else:
                        self.log_error()
                 

interpreter = NaLangInterpreter()
code = """val string greeting
assign greeting "Hello, World!"
valLog(greeting)"""

interpreter.run(code)