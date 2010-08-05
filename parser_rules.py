import re
def ens(t):
    if len(t) > 1:
        raise Exception('not supported')
    else:
        t[0] = ''

def ej(t, m = " "):
    if len(t) > 1:
        t[0] = m.join(t[1:])
    else:
        t[0] = ''
        
def j(t, m = " "):
    t[0] = m.join(t[1:])

def j1(t, sep = " "):
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + sep + t[3]

def ns():
    raise Exception('not supported')

def i(s):
    return i.re.sub("    ", s, 0)

i.re = re.compile(r'^(?=.)', re.MULTILINE)

#def p_file(t):
#    '''file : program
#            | module
#    '''
#    t[0] = t[1]

#def p_program(t):
#    '''program : program_heading semicolon block DOT
#    '''
#    t[0] = t[1]

#def p_program_heading(t):
#    '''program_heading : PROGRAM identifier
# | PROGRAM identifier LPAREN identifier_list RPAREN
#    '''
#    t[0] = t[1]

def p_identifier_list(t):
    '''identifier_list : identifier_list comma identifier
                       | identifier
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_block(t):
    'block : label_declaration_part constant_definition_part type_definition_part variable_declaration_part procedure_and_function_declaration_part statement_part'
    t[0] = "{\n" + i(''.join(t[1:])) + "}\n"

#def p_module(t):
#    '''module : constant_definition_part
# type_definition_part
# variable_declaration_part
# procedure_and_function_declaration_part
#    '''
#    t[0] = t[1]

def p_label_declaration_part(t):
    '''label_declaration_part : LABEL label_list semicolon
        |
    '''
    ens(t)

def p_label_list(t):
    '''label_list : label_list comma label
        | label
    '''
    ns()

def p_label(t):
    'label : DIGSEQ'
    ns()

def p_constant_definition_part(t):
    '''constant_definition_part : CONST constant_list
        |
    '''
    if len(t) > 1:
        t[0] = t[2]
    else:
        t[0] = ''

def p_constant_list(t):
    '''constant_list : constant_list constant_definition
        | constant_definition
    '''
    ej(t, "\n")

def p_constant_definition(t):
    'constant_definition : identifier EQUAL cexpression semicolon'
    t[0] = "const " + " ".join(t[1:])

def p_cexpression(t):
    '''cexpression : csimple_expression
        | csimple_expression relop csimple_expression
    '''
    j(t)

def p_csimple_expression(t):
    '''csimple_expression : cterm
        | csimple_expression addop cterm
    '''
    j(t)

def p_cterm(t):
    '''cterm : cfactor
        | cterm mulop cfactor
    '''
    j(t)

def p_cfactor(t):
    '''cfactor : sign cfactor
        | cexponentiation
    '''
    j(t, '')

def p_cexponentiation(t):
    '''cexponentiation : cprimary
        | cprimary STARSTAR cexponentiation
    '''
    j(t, '')

def p_cprimary(t):
    '''cprimary : identifier
        | LPAREN cexpression RPAREN
        | unsigned_constant
        | NOT cprimary
    '''
    j(t)

def p_constant(t):
    '''constant : non_string
        | sign non_string
        | CHARACTER_STRING
    '''
    j(t, '')

def p_sign(t):
    '''sign : PLUS
        | MINUS
    '''
    t[0] = t[1]

def p_non_string(t):
    '''non_string : DIGSEQ
        | identifier
        | REALNUMBER
    '''
    t[0] = t[1]

def p_type_definition_part(t):
    '''type_definition_part : TYPE type_definition_list
        |
    '''
    ens(t)

def p_type_definition_list(t):
    '''type_definition_list : type_definition_list type_definition
        | type_definition
    '''
    ns()

def p_type_definition(t):
    'type_definition : identifier EQUAL type_denoter semicolon'
    ns()

def p_type_denoter(t):
    '''type_denoter : identifier
        | new_type
    '''
    t[0] = t[1]

def p_new_type(t):
    '''new_type : new_ordinal_type
        | new_structured_type
        | new_pointer_type
    '''
    ns()

def p_new_ordinal_type(t):
    '''new_ordinal_type : enumerated_type
        | subrange_type
    '''
    ns()

def p_enumerated_type(t):
    'enumerated_type : LPAREN identifier_list RPAREN'
    ns()

def p_subrange_type(t):
    'subrange_type : constant DOTDOT constant'
    ns()

def p_new_structured_type(t):
    '''new_structured_type : structured_type
        | PACKED structured_type
    '''
    ns()

def p_structured_type(t):
    '''structured_type : array_type
        | record_type
        | set_type
        | file_type
    '''
    ns()

def p_array_type(t):
    'array_type : ARRAY LBRAC index_list RBRAC OF component_type'
    ns()

def p_index_list(t):
    '''index_list : index_list comma index_type
        | index_type
    '''
    ns()

def p_index_type(t):
    'index_type : ordinal_type'
    ns()

def p_ordinal_type(t):
    '''ordinal_type : new_ordinal_type
        | identifier
    '''
    ns()

def p_component_type(t):
    'component_type : type_denoter'
    ns()

def p_record_type(t):
    '''record_type : RECORD record_section_list end
        | RECORD record_section_list semicolon variant_part end
        | RECORD variant_part end
    '''
    ns()

def p_record_section_list(t):
    '''record_section_list : record_section_list semicolon record_section
        | record_section
    '''
    ns()

def p_record_section(t):
    'record_section : identifier_list COLON type_denoter'
    ns()

def p_variant_part(t):
    '''variant_part : CASE variant_selector OF variant_list semicolon
        | CASE variant_selector OF variant_list
        |
    '''
    ns()

def p_variant_selector(t):
    '''variant_selector : tag_field COLON tag_type
        | tag_type
    '''
    ns()

def p_variant_list(t):
    '''variant_list : variant_list semicolon variant
        | variant
    '''
    ns()

def p_variant(t):
    '''variant : case_constant_list COLON LPAREN record_section_list RPAREN
             | case_constant_list COLON LPAREN record_section_list semicolon variant_part RPAREN
             | case_constant_list COLON LPAREN variant_part RPAREN
    '''
    ns()

def p_case_constant_list(t):
    '''case_constant_list : case_constant_list comma case_constant
        | case_constant
    '''
    ns()

def p_case_constant(t):
    '''case_constant : constant
        | constant DOTDOT constant
    '''
    ns()

def p_tag_field(t):
    'tag_field : identifier'
    t[0] = t[1]

def p_tag_type(t):
    'tag_type : identifier'
    t[0] = t[1]

def p_set_type(t):
    'set_type : SET OF base_type'
    ns()

def p_base_type(t):
    'base_type : ordinal_type'
    t[0] = t[1]

def p_file_type(t):
    'file_type : PFILE OF component_type'
    ns()

def p_new_pointer_type(t):
    'new_pointer_type : UPARROW domain_type'
    ns()

def p_domain_type(t):
    'domain_type : identifier'
    ns()

def p_variable_declaration_part(t):
    '''variable_declaration_part : VAR variable_declaration_list semicolon
        |
    '''
    if len(t) == 1:
        t[0] = ''
    else:
        t[0] = t[2] + "\n"

def p_variable_declaration_list(t):
    '''variable_declaration_list : variable_declaration_list semicolon variable_declaration
        | variable_declaration
    '''
    if len(t)==2:
        t[0] = t[1]
    else:
        t[0] = t[1] + "\n" + t[3]

def p_variable_declaration(t):
    'variable_declaration : identifier_list COLON type_denoter'
    t[0] = ""
    for id in t[1]:
        t[0] += "var " + id + " = null; /*" + t[3] + "*/\n"

def p_procedure_and_function_declaration_part(t):
    '''procedure_and_function_declaration_part : proc_or_func_declaration_list semicolon
        |
    '''
    if len(t)==1:
        t[0] = ''
    else:
        t[0] = t[1] + "\n"

def p_proc_or_func_declaration_list(t):
    '''proc_or_func_declaration_list : proc_or_func_declaration_list semicolon proc_or_func_declaration
        | proc_or_func_declaration
    '''
    j1(t, "\n")

def p_proc_or_func_declaration(t):
    '''proc_or_func_declaration : procedure_declaration
        | function_declaration
    '''
    t[0] = t[1]

def p_procedure_declaration(t):
    '''procedure_declaration : procedure_heading semicolon directive
        | procedure_heading semicolon procedure_block
    '''
    ns()

def p_procedure_heading(t):
    '''procedure_heading : procedure_identification
        | procedure_identification formal_parameter_list
    '''
    ns()

def p_directive(t):
    '''directive : FORWARD
        | EXTERNAL 
        | EXTERNAL CHARACTER_STRING
    '''
    if len(t) == 3:
        t[0] = "result = external(" + t[2] + ");"
    else:
        ns()

def p_formal_parameter_list(t):
    'formal_parameter_list : LPAREN formal_parameter_section_list RPAREN'
    j(t, '')

def p_formal_parameter_section_list(t):
    '''formal_parameter_section_list : formal_parameter_section_list semicolon formal_parameter_section
        | formal_parameter_section
    '''
    j1(t, ", ")

def p_formal_parameter_section(t):
    '''formal_parameter_section : value_parameter_specification
        | variable_parameter_specification
        | procedural_parameter_specification
        | functional_parameter_specification
    '''
    t[0] = t[1]

def p_value_parameter_specification(t):
    'value_parameter_specification : identifier_list COLON identifier'
    t[0] = "{0} /*{1}*/".format(", ".join(t[1]), t[3])

def p_variable_parameter_specification(t):
    'variable_parameter_specification : VAR identifier_list COLON identifier'
    t[0] = "{0} /*{1}, out*/".format(", ".join(t[2]), t[4])

def p_procedural_parameter_specification(t):
    'procedural_parameter_specification : procedure_heading'
    t[0] = t[1]

def p_functional_parameter_specification(t):
    'functional_parameter_specification : function_heading'
    t[0] = t[1]

def p_procedure_identification(t):
    'procedure_identification : PROCEDURE identifier'
    ns()

def p_procedure_block(t):
    'procedure_block : block'
    t[0] = t[1]

def p_function_declaration(t):
    '''function_declaration : function_heading semicolon directive
        | function_identification semicolon function_block
        | function_heading semicolon function_block
    '''
    fheading, funcid = t[1]
    t[0] = """{0}{{
    var result = null;
    var {1} = null;
    
{2}
    
    return result || {1};
}}
""".format(fheading, funcid, i(t[3]))

def p_function_heading(t):
    '''function_heading : FUNCTION identifier COLON result_type
        | FUNCTION identifier formal_parameter_list COLON result_type
    '''
    if len(t) == 5:
        t[0] = "function {0}() /* returns {1} */\n".format(t[2], t[4])
    else:
        t[0] = "function {0}{1} /* returns {2} */\n".format(t[2], t[3], t[5])
    t[0] = (t[0], t[2])

def p_result_type(t):
    'result_type : identifier'
    t[0] = t[1]

def p_function_identification(t):
    'function_identification : FUNCTION identifier'
    t[0] = "function {0}()".format(t[2])

def p_function_block(t):
    'function_block : block'
    t[0] = t[1]

def p_statement_part(t):
    'statement_part : compound_statement'
    t[0] = t[1]

def p_compound_statement(t):
    'compound_statement : pbegin statement_sequence end'
    t[0] = t[2]

def p_statement_sequence(t):
    '''statement_sequence : statement_sequence semicolon statement
        | statement
    '''
    if len(t)==2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[3]

def p_statement(t):
    '''statement : open_statement
        | closed_statement
    '''
    t[0] = t[1]

def p_open_statement(t):
    '''open_statement : label COLON non_labeled_open_statement
        | non_labeled_open_statement
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        ns()

def p_closed_statement(t):
    '''closed_statement : label COLON non_labeled_closed_statement
        | non_labeled_closed_statement
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        ns()

def p_non_labeled_closed_statement(t):
    '''non_labeled_closed_statement : assignment_statement
                             | procedure_statement
                             | goto_statement
                             | compound_statement
                             | case_statement
                             | repeat_statement
                             | closed_with_statement
                             | closed_if_statement
                             | closed_while_statement
                             | closed_for_statement
                             |
    '''
    if len(t) == 1:
        t[0] = ''
    else:
        t[0] = t[1] + "\n"

def p_non_labeled_open_statement(t):
    '''non_labeled_open_statement : open_with_statement
        | open_if_statement
        | open_while_statement
        | open_for_statement
    '''
    t[0] = t[1] + "\n"

def p_repeat_statement(t):
    'repeat_statement : REPEAT statement_sequence UNTIL boolean_expression'
    ns()

def p_open_while_statement(t):
    'open_while_statement : WHILE boolean_expression DO open_statement'
    t[0] = "while ({0})\n{1}".format(t[2], i(t[4]))

def p_closed_while_statement(t):
    'closed_while_statement : WHILE boolean_expression DO closed_statement'
    t[0] = "while ({0}) {{\n{1}}}".format(t[2], i(t[4]))

def p_open_for_statement(t):
    'open_for_statement : FOR control_variable assignment initial_value direction final_value DO open_statement'
    #op = '++' if t[5].lower() == 'to' else '--'
    #t[0] = "for ({0} = {1}); {0} <= {2}; {0}{4})\n{3}".format(t[2], t[4], t[6], t[8], op)
    ns()

def p_closed_for_statement(t):
    'closed_for_statement : FOR control_variable assignment initial_value direction final_value DO closed_statement'
    op = '++' if t[5].lower() == 'to' else '--'
    t[0] = "for ({0} = {1}; {0} <= {2}; {0}{4}) {{\n{3}}}".format(t[2], t[4], t[6], i(t[8]), op)

def p_open_with_statement(t):
    'open_with_statement : WITH record_variable_list DO open_statement'
    ns()

def p_closed_with_statement(t):
    'closed_with_statement : WITH record_variable_list DO closed_statement'
    ns()

def p_open_if_statement(t):
    '''open_if_statement : IF boolean_expression THEN statement
        | IF boolean_expression THEN closed_statement ELSE open_statement
    '''
    if len(t)==5:
        t[0] = "if ({0}) {{\n{1}}}".format(t[2], i(t[4]))
    else:
        t[0] = "if ({0}) {{\n{1}}} else {{\n{2}}}".format(t[2], i(t[4]), t[6])
        

def p_closed_if_statement(t):
    'closed_if_statement : IF boolean_expression THEN closed_statement ELSE closed_statement'
    t[0] = "if ({0}) {{\n{1}}} else {{\n{2}}}".format(t[2], i(t[4]), i(t[6]))

def p_assignment_statement(t):
    'assignment_statement : variable_access assignment expression'
    j(t)
    t[0] += ";"

def p_variable_access(t):
    '''variable_access : identifier
        | indexed_variable
        | field_designator
        | variable_access UPARROW
    '''
    j(t, '')

def p_indexed_variable(t):
    'indexed_variable : variable_access LBRAC index_expression_list RBRAC'
    j(t)

def p_index_expression_list(t):
    '''index_expression_list : index_expression_list comma index_expression
        | index_expression
    '''
    if len(t)==2:
        t[0] = t[1]
    else:
        t[0] = "{0}][{1}".format(t[1], t[3])

def p_index_expression(t):
    'index_expression : expression'
    t[0] = t[1]

def p_field_designator(t):
    'field_designator : variable_access DOT identifier'
    j(t, '')

def p_actual_parameter_list(t):
    '''actual_parameter_list : actual_parameter_list comma actual_parameter
        | actual_parameter
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_actual_parameter(t):
    '''actual_parameter : expression
        | expression COLON expression
        | expression COLON expression COLON expression
    '''
    if (len(t)==2):
        t[0] = t[1]
    else:
        ns()

def p_goto_statement(t):
    'goto_statement : GOTO label'
    ns()

def p_case_statement(t):
    '''case_statement : CASE case_index OF case_list_element_list end
         | CASE case_index OF case_list_element_list SEMICOLON end
         | CASE case_index OF case_list_element_list semicolon otherwisepart statement end
         | CASE case_index OF case_list_element_list semicolon otherwisepart statement SEMICOLON end
    '''
    ns()

def p_case_index(t):
    'case_index : expression'
    ns()

def p_case_list_element_list(t):
    '''case_list_element_list : case_list_element_list semicolon case_list_element
        | case_list_element
    '''
    ns()

def p_case_list_element(t):
    'case_list_element : case_constant_list COLON statement'
    ns()

def p_otherwisepart(t):
    '''otherwisepart : OTHERWISE
        | OTHERWISE COLON
    '''
    ns()

def p_control_variable(t):
    'control_variable : identifier'
    t[0] = t[1]

def p_initial_value(t):
    'initial_value : expression'
    t[0] = t[1]

def p_direction(t):
    '''direction : TO
        | DOWNTO
    '''
    t[0] = t[1]

def p_final_value(t):
    'final_value : expression'
    t[0] = t[1]

def p_record_variable_list(t):
    '''record_variable_list : record_variable_list comma variable_access
        | variable_access
    '''
    ns()

def p_boolean_expression(t):
    'boolean_expression : expression'
    t[0] = t[1]

def p_expression(t):
    '''expression : simple_expression
        | simple_expression relop simple_expression
    '''
    j(t)

def p_simple_expression(t):
    '''simple_expression : term
        | simple_expression addop term
    '''
    j(t)

def p_term(t):
    '''term : factor
        | term mulop factor
    '''
    j(t, '')

def p_factor(t):
    '''factor : sign factor
        | exponentiation
    '''
    j(t, '')

def p_exponentiation(t):
    '''exponentiation : primary
        | primary STARSTAR exponentiation
    '''
    j(t, '')

def p_primary(t):
    '''primary : variable_access
        | unsigned_constant
        | function_designator
        | set_constructor
        | LPAREN expression RPAREN
        | NOT primary
    '''
    j(t, ' ')

def p_unsigned_constant(t):
    '''unsigned_constant : unsigned_number
        | CHARACTER_STRING
        | NIL
    '''
    t[0] = t[1]

def p_unsigned_number(t):
    '''unsigned_number : unsigned_integer 
                       | unsigned_real
    '''
    t[0] = t[1]

def p_unsigned_integer(t):
    'unsigned_integer : DIGSEQ'
    t[0] = t[1]

def p_unsigned_real(t):
    'unsigned_real : REALNUMBER'
    t[0] = t[1]

def p_set_constructor(t):
    '''set_constructor : LBRAC member_designator_list RBRAC
        | LBRAC RBRAC
    '''
    ns()

def p_member_designator_list(t):
    '''member_designator_list : member_designator_list comma member_designator
        | member_designator
    '''
    ns()

def p_member_designator(t):
    '''member_designator : member_designator DOTDOT expression
        | expression
    '''
    ns()

def p_addop(t):
    '''addop : PLUS
            | MINUS
            | OR
    '''
    t[0] = t[1]

def p_mulop(t):
    '''mulop : STAR
        | slash
        | div
        | mod
        | and
        | shl
        | shr
    '''
    t[0] = t[1]

def p_relop(t):
    '''relop : equal
        | notequal
        | LT
        | GT
        | LE
        | GE
        | IN
    '''
    t[0] = t[1]

def p_identifier(t):
    'identifier : IDENTIFIER'
    t[0] = t[1].lower()

def p_semicolon(t):
    'semicolon : SEMICOLON'
    t[0] = t[1]

def p_comma(t):
    'comma : COMMA'
    t[0] = t[1]
    
def p_params(t):
    'params : LPAREN actual_parameter_list RPAREN'
    t[0] = t[2]

def p_procedure_statement(t):
    '''procedure_statement : identifier params
        | identifier
    '''
    if len(t) == 2:
        t[0] = t[1] + '()'
    else:
        p_function_designator(t)

def p_function_designator(t):
    'function_designator : identifier params'
    funcmap = {
        'inttostr': "'' + ",
        'intpower': 'Math.pow',
        'round': 'Math.round',
        'roundex': 'Math.round',
        'abs': 'Math.abs',
        'arctan': 'Math.atan',
        'insert': t[2][1] + ' = insert' if len(t[2])>1 else None,
    }
    t[0] = funcmap.get(t[1].lower(), t[1]) + '(' + ', '.join(t[2]) + ')'


def p_REALNUMBER(t):
    'REALNUMBER : DIGSEQ DOT DIGSEQ'
    j(t, '')
    
def p_pbegin(t):
    'pbegin : PBEGIN'
    t[0] = ""

def p_end(t):
    'end : END'
    t[0] = ""
    
def p_assignment(t):
    'assignment : ASSIGNMENT'
    t[0] = '='
    
def p_and(t):
    'and : AND'
    t[0] = '&&'

def p_div(t):
    'div : DIV'
    t[0] = '/'

def p_mod(t):
    'mod : MOD'
    t[0] = '%'

def p_slash(t):
    'slash : SLASH'
    t[0] = '/1.0/'

def p_shl(t):
    'shl : SHL'
    t[0] = '<<'

def p_shr(t):
    'shr : SHR'
    t[0] = '>>'
    
def p_notequal(t):
    'notequal : NOTEQUAL'
    t[0] = '!='

def p_equal(t):
    'equal : EQUAL'
    t[0] = '=='