
command_words = ["assignto", "goto", "move", "turn", "face", "put", "pick", "movetothe", "moveindir", "jumptothe", "jumpindir", "nop"]
condition_words = ["facing", "canput", "canpick", "canmoveindir", "canjumpindir", "canmovetothe", "canjumptothe", "not"]
reserved_chars = ["[", "]", ":", "|", ",", ";"]
structure_words = ["if", "while", "repeat"]
init_keyword = "robot_r"
procs_keyword = "procs"

import rules_conditionals as rcond
import rules_procedures as rpcd
import rules_structures as rstr
import rules_commands as rcom
import rules_blocks as rbck



def main_executer(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    if tokens[0] in condition_words:
        return execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in command_words:
        return execute_verify_command(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in structure_words:
        xblock = True
        return execute_verify_structure(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in procs:
        xblock = True
        isproc = True
        return execute_verify_procedure(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "[":
        tokens.pop(0)
        xblock = True
        return execute_verify_block(tokens, vars, xblock, isproc, procs, procvars)
    else:
        return False


def internal_executer(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    if tokens[0] in condition_words:
        return execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in command_words:
        return execute_verify_command(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in structure_words:
        xblock = True
        return execute_verify_structure(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] in procs:
        return execute_verify_secprocedure(tokens, vars, xblock, isproc, procs, procvars)
    else:
        return False


def execute_verify_conditional(tokens, vars, xblock, isproc, procs, procvars):
    
    if tokens[0] == "facing":
        tokens.pop(0)
        return rcond.verify_facing(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canput":
        tokens.pop(0)
        return rcond.verify_canPut_canPick(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canpick":
        tokens.pop(0)
        return rcond.verify_canPut_canPick(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canmoveindir":
        tokens.pop(0)
        return rcond.verify_canMoveinDir_canJumpinDir(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canjumpindir":
        tokens.pop(0)
        return rcond.verify_canMoveinDir_canJumpinDir(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canmovetothe":
        tokens.pop(0)
        return rcond.verify_canMovetoThe_canjumptoThe(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "canjumptothe":
        tokens.pop(0)
        return rcond.verify_canMovetoThe_canjumptoThe(tokens, vars, xblock, isproc, procs, procvars)
    else:
        tokens.pop(0)
        return rcond.verify_not(tokens, vars, xblock, isproc, procs, procvars)


def execute_verify_command(tokens, vars, xblock, isproc, procs, procvars): 

    if tokens[0] == "assignto":
        tokens.pop(0)
        return rcom.verify_assignTo(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "goto":
        tokens.pop(0)
        return rcom.verify_goTo(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "move":
        tokens.pop(0)
        return rcom.verify_move(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "turn":
        tokens.pop(0)
        return rcom.verify_turn(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "face":
        tokens.pop(0)
        return rcom.verify_face(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "put":
        tokens.pop(0)
        return rcom.verify_put_pick(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "pick":
        tokens.pop(0)
        return rcom.verify_put_pick(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "movetothe":
        tokens.pop(0)
        return rcom.verify_moveToThe(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "moveindir":
        tokens.pop(0)
        return rcom.verify_moveInDir(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "jumptothe":
        tokens.pop(0)
        return rcom.verify_jumpToThe(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "jumpindir":
        tokens.pop(0)
        return rcom.verify_jumpInDir(tokens, vars, xblock, isproc, procs, procvars)
    else:
        tokens.pop(0)
        return rcom.verify_nop(tokens, vars, xblock, isproc, procs, procvars)


def execute_verify_structure(tokens, vars, xblock, isproc, procs, procvars):

    if tokens[0] == "if":
        tokens.pop(0)
        return rstr.verify_conditional(tokens, vars, xblock, isproc, procs, procvars)
    elif tokens[0] == "while":
        tokens.pop(0)
        return rstr.verify_loop(tokens, vars, xblock, isproc, procs, procvars)
    else:
        tokens.pop(0)
        return rstr.verify_repeatTimes(tokens, vars, xblock, isproc, procs, procvars)


def execute_verify_procedure(tokens, vars, xblock, isproc, procs, procvars):

    name = tokens[0]
    tokens.pop(0)

    return rpcd.verify_procedure_structure(tokens, vars, xblock, isproc, procs, procvars)


def execute_verify_secprocedure(tokens, vars, xblock, isproc, procs, procvars):

    name = tokens[0]
    tokens.pop(0)

    return rpcd.verify_procedure(tokens, vars, xblock, isproc, procs, procvars)


def execute_verify_block(tokens, vars, xblock, isproc, procs, procvars): ###LISTA###

    return rbck.verify_block(tokens, vars, xblock, isproc, procs, procvars)


