
import finders as fdrs

def verify_keyword(tokens): 

    if tokens[0] == "robot_r":
        tokens.pop(0)
        return True
    else:
        return False


def verify_procedures(tokens): ###LISTA###

    if "procs" in tokens:
        return True
    else:
        return False


#FUNCIONES PARA VERIFICAR VARIABLES


def verify_parameters_procedures(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    expected = procvars
    verify, given = fdrs.find_passed_parameters(tokens, vars, xblock, isproc, procs, procvars)
    
    if verify:
        if len(given) == len(expected):

            for index in range(0, len(given)):
                if isinstance(given[index], int):
                    pass
                elif given[index] in vars:
                    pass
                else:
                    return False

        else:
            return False
    else:
        return False
