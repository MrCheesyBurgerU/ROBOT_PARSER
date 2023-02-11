
import executers as xctr

def verify_block(tokens, vars, xblock, isproc, procs, procvars): 

    verify = xctr.internal_executer(tokens, vars, xblock, isproc, procs, procvars)

    return verify
        
