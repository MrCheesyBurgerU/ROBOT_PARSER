
command_words = ["assignto", "goto", "move", "turn", "face", "put", "pick", "movetothe", "moveindir", "jumptothe", "jumpindir", "nop"]
condition_words = ["facing", "canput", "canpick", "canmoveindir", "canjumpindir", "canmovetothe", "canjumptothe", "not"]
reserved_chars = ["[", "]", ":", "|", ",", ";"]
structure_words = ["if", "while", "repeat"]
init_keyword = "robot_r"
procs_keyword = "procs"

import executers as xctr

def verify_conditional(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in condition_words:
            verify = xctr.execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
            if verify: 
                if tokens[0] == "then":
                    tokens.pop(0)
                    if tokens[0] == ":":
                        tokens.pop(0)
                        if tokens[0] =="[":
                            tokens.pop(0)
                            verify = xctr.execute_verify_block(tokens, vars, xblock, isproc, procs, procvars)
                            if verify:
                                if tokens[0] == "else":
                                    tokens.pop(0)
                                    if tokens[0] == ":":
                                        tokens.pop(0)
                                        if tokens[0] == "[":
                                            tokens.pop(0)
                                            verify = xctr.execute_verify_block(tokens, vars, xblock, isproc, procs, procvars)
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
        else:
            return False
    else:
        return False
    

def verify_loop(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in condition_words:
            verify = xctr.execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
            if verify:
                if tokens[0] == "do":
                    tokens.pop(0)
                    if tokens[0] == ":":
                        tokens.pop(0)
                        if tokens[0] == "[":
                            tokens.pop(0)
                            verify = xctr.execute_verify_block(tokens, vars, xblock, isproc, procs, procvars)
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
            else:
                return False
        else:
            return False
    else:
        return False


def verify_repeatTimes(tokens, vars, xblock, isproc, procs, procvars):

    if tokens[0] == ":":
        tokens.pop(0)
        if tokens[0] in vars or isinstance(tokens[0], int):
            tokens.pop(0)
            if tokens[0] == "[":
                tokens.pop(0)
                verify = xctr.execute_verify_block(tokens, vars, xblock, isproc, procs, procvars)
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
