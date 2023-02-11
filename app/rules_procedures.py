
import verifiers as vrfs
import executers as xctr
import finders as fdrs


def verify_procedure_structure(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == "[":
        xblock = True
        tokens.pop(0)
        if tokens[0] == "|":
            tokens.pop(0)
            verify, procvars = fdrs.find_parameters_procedures(tokens, vars, xblock, isproc, procs, procvars)
            if verify:
                verify = xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                if verify:
                    return True
                else:
                        return False
            else:
                    return False
        else:
            return False
    else:
        return False


def verify_procedure(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    if tokens[0] == ":":
        tokens.pop(0)
        flag = True
        while flag:
            if isinstance(tokens[0], int) or tokens[0] in vars:
                tokens.pop(0)
                if tokens[0] == ",":
                    tokens.pop(0)
                else:
                    flag = False
                    verify = True
            else:
                flag = False
                verify = False
        if verify:
            if tokens[0] == ";":
                tokens.pop(0)
                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
            elif tokens[0] == "]":
                tokens.pop(0)
                return True
            else:
                return True
        else:
            return False
    else:
        return False