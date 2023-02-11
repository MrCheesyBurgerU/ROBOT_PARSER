
turn_words = ["right", "left", "around", "back", "front"]
cardinal_words = ["west", "north", "south", "east"]
objects_words = ["chips", "balloons"]

import executers as xctr

def verify_facing(tokens, vars, xblock, isproc, procs, procvars):

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in cardinal_words:
            tokens.pop(0)
            if tokens[0] == ";":
                tokens.pop(0)
                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
            elif xblock and not isproc:
                if tokens[0] == "]":
                    return True
                else:
                    return True
            elif isproc:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def verify_canPut_canPick(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
                if tokens[0] in objects_words:
                    tokens.pop(0)
                    if tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    elif xblock and not isproc:
                        if tokens[0] == "]":
                            return True
                        else:
                            return True
                    elif isproc:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def verify_canMoveinDir_canJumpinDir(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
                if tokens[0] in cardinal_words:
                    tokens.pop(0)
                    if tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    elif xblock and not isproc:
                        if tokens[0] == "]":
                            return True
                        else:
                            return True
                    elif isproc:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def verify_canMovetoThe_canjumptoThe(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
                if tokens[0] in turn_words:
                    tokens.pop(0)
                    if tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    elif xblock and not isproc:
                        if tokens[0] == "]":
                            return True
                        else:
                            return True
                    elif isproc:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def verify_not(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        verify = xctr.execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
        if verify:
            return True
        else:
            return False
    else:
        return False
        