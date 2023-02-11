
turn_words = ["right", "left", "around", "back", "front"]
cardinal_words = ["west", "north", "south", "east"]
objects_words = ["chips", "balloons"]

import executers as xctr

def verify_assignTo(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if isinstance(tokens[0], int):
            tokens.pop(0)                                                   
            if tokens[0] == ",":
                tokens.pop(0)
                if tokens[0] in vars or tokens in procvars:
                    tokens.pop(0)
                    if tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    elif xblock and not isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True     
                    elif isproc:
                        tokens.pop(0)
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


def verify_goTo(tokens, vars, xblock, isproc, procs, procvars):

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
            tokens.pop(0)
            if tokens[0] == ",":
                tokens.pop(0)
                if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
                    tokens.pop(0)
                    if tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    elif xblock and not isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if tokens[0] == "]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return True
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True     
                    elif isproc:
                        tokens.pop(0)
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


def verify_move(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int) or tokens[0] in procvars:
            tokens.pop(0)
            if tokens[0] == ";":
                tokens.pop(0)
                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
            elif xblock and not isproc:
                if tokens[0] == "]":
                    tokens.pop(0)
                    return True
                else:
                    return False
            elif xblock and isproc:
                if tokens[0] == "]":
                    tokens.pop(0)
                    if isproc and tokens[0] =="]":
                        tokens.pop(0)
                        return True
                    elif tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    return True     
            elif isproc:
                tokens.pop(0)
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def verify_turn(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
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
                    return False
            elif xblock and isproc:
                if tokens[0] == "]":
                    tokens.pop(0)
                    if isproc and tokens[0] =="]":
                        tokens.pop(0)
                        return True
                    elif tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    return True     
            elif isproc:
                tokens.pop(0)
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def verify_face(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in cardinal_words:
            tokens.pop(0)
            if tokens[0] == ";":
                tokens.pop(0)
                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
            elif xblock and not isproc:
                if tokens[0] == "]":
                    tokens.pop(0)
                    return True
                else:
                    return False
            elif xblock and isproc:
                if tokens[0] == "]":
                    tokens.pop(0)
                    if isproc and tokens[0] =="]":
                        tokens.pop(0)
                        return True
                    elif tokens[0] == ";":
                        tokens.pop(0)
                        return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                    return True     
            elif isproc:
                tokens.pop(0)
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def verify_put_pick(tokens, vars, xblock, isproc, procs, procvars): 

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
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True     
                    elif isproc:
                        tokens.pop(0)
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


def verify_moveToThe(tokens, vars, xblock, isproc, procs, procvars): 

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
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True    
                    elif isproc:
                        tokens.pop(0)
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


def verify_moveInDir(tokens, vars, xblock, isproc, procs, procvars): 

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
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True     
                        else:
                            return False
                    elif isproc:
                        tokens.pop(0)
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


def verify_jumpToThe(tokens, vars, xblock, isproc, procs, procvars): 

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
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True    
                    elif isproc:
                        tokens.pop(0)
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


def verify_jumpInDir(tokens, vars, xblock, isproc, procs, procvars): 

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
                            tokens.pop(0)
                            return True
                        else:
                            return False
                    elif xblock and isproc:
                        if tokens[0] == "]":
                            tokens.pop(0)
                            if isproc and tokens[0] =="]":
                                tokens.pop(0)
                                return True
                            elif tokens[0] == ";":
                                tokens.pop(0)
                                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                            return True     
                    elif isproc:
                        tokens.pop(0)
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
    

def verify_nop(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] == ";":
                tokens.pop(0)
                return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
        elif xblock and not isproc:
            if tokens[0] == "]":
                tokens.pop(0)
                return True
            else:
                return False
        elif xblock and isproc:
            if tokens[0] == "]":
                tokens.pop(0)
                if isproc and tokens[0] =="]":
                    tokens.pop(0)
                    return True
                elif tokens[0] == ";":
                    tokens.pop(0)
                    return xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)
                else:
                    return xctr.main_executer(tokens, vars, xblock, isproc, procs, procvars)
            return True     
        elif isproc:
            tokens.pop(0)
            return True
        elif not isproc and not xblock:
            tokens.pop(0)
            return True
        else:
            return False
    else:
        return False