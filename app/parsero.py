import custom_tokenizer as tknz
import raise_error as error
import executers as xctrs
import verifiers as vrfs
import finders as fdrs


def load_code (file_path): 
    
    file = open(file_path, "r+", encoding="utf-8")

    code = file.read()
    code = code.replace("\n", " ")
    code = code.lower()

    file.close

    tokens = tknz.tokenize(code)
    clear_tokens = tknz.castInteger(tokens)

    return clear_tokens 


def parse(tokens):

    if vrfs.verify_keyword(tokens):

        vars_verifier, vars = fdrs.find_variables(tokens)

        if vrfs.verify_procedures(tokens):
            procedures = fdrs.find_procedures(tokens, vars)
            tokens.pop(tokens.index("procs"))
        else:
            procedures = []

        if vars_verifier:
            
            breaker = True

            try:
                while breaker:

                    xblock = False
                    isproc = False
                    procvars = []

                    breaker = xctrs.main_executer(tokens, vars, xblock, isproc, procedures, procvars)

                error.raise_error(tokens)

            except:
                error.raise_error(tokens)

        else:
            error.raise_error(tokens)
    else:
        error.raise_error(tokens)

    
        

