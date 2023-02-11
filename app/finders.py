

command_words = ["assignto", "goto", "move", "turn", "face", "put", "pick", "movetothe", "moveindir", "jumptothe", "jumpindir", "nop"]
condition_words = ["facing", "canput", "canpick", "canmoveindir", "canjumpindir", "canmovetothe", "canjumptothe", "not"]
reserved_chars = ["[", "]", ":", "|", ",", ";"]
structure_words = ["if", "while", "repeat"]
init_keyword = "robot_r"
procs_keyword = "procs"


def find_variables(tokens):

    vars = []
    
    if "vars" in tokens:

        tokens.pop(0)
        flag = True

        
        while flag:
                
            if tokens[0] not in reserved_chars:

                buffer = tokens[0]
                tokens.pop(0)

                if len(tokens) > 0:
                    if tokens[0] == ",":
                        
                        vars.append(buffer)
                        tokens.pop(0)
                    
                    elif tokens[0] != ",":
                        
                        vars.append(buffer)
                        flag = False

                        return True, vars
                
                    else:
                        
                        return False, vars
                else:
                    vars.append(buffer)
                    flag = False

                    return True, vars
            else:
                
                flag = False, vars
                return False, vars
        
    else:
        return True, vars


def find_procedures(tokens, vars):

    init_index = tokens.index("procs") 
    procedures = []

    for index in range(init_index, len(tokens)):

        token = tokens[index]

        if (token not in vars) and (token not in command_words) and (token not in structure_words) and (token not in condition_words) and (token not in reserved_chars) and (type(token) != int) and (token != init_keyword) and (token != "vars") and (token != procs_keyword):
            procedures.append(token)
    
    return procedures
        

def find_parameters_procedures(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    flag = True
    procedure_vars = []

    while flag:

        if isinstance(tokens[0], str) and tokens[0] not in reserved_chars:
            procedure_vars.append(tokens[0])
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
            elif tokens[0] == "|":
                tokens.pop(0)
                procvars = procedure_vars
                flag = False
                return True, procvars
            else:
                flag = False
                return False, procvars
        else:
            flag = False
            if tokens[0] == "|":
                tokens.pop(0)
                return True, procedure_vars
            else:
                return False


def find_passed_parameters(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    flag = True
    passed_vars = []

    while flag:
        if tokens[0] in vars or isinstance(tokens[0], int):
            passed_vars.append(tokens[0])
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
            else:
                flag = False
                return True, passed_vars
        else:
            return False, passed_vars
