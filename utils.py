import IPython
from nose.tools import assert_equal, ok_
from propositional_state_logic import *
from sat_solver import *

def test_ok():
    """ If execution gets to this point, print out a happy message """
    try:
        from IPython.display import display_html
        display_html("""<div class="alert alert-success">
        <strong>Tests passed!!</strong>
        </div>""", raw=True)
    except:
        print("Tests passed!!")


### Helper Functions ###
def get_all_children(d):
    for key, value in d.items():
        yield key
        if isinstance(value, dict):
            yield from get_all_children(value)

def is_conflict(sat, candidate):
    return not sat.check_consistency(candidate)[0]
### End Helper Functions ###

#Check for Problem #1

def check_validity(fn):
    #Solution for Cases 1-26
    solution_list=[False, False, True, True, False, True, True, True, True, False, False, True, 
                   True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    index=0
    p = Problem()
    T1 = p.add_variable('thruster', type='finite_domain', domain=['thrust', 'nothrust'])
    R1 = p.add_variable('runthruster', type='finite_domain', domain=['on', 'off'])
    P3 = p.add_variable('pressure', type='finite_domain', domain=['high', 'low'])
    p.add_constraint('runthruster=on & pressure=high => thruster=thrust')
    p.add_constraint('runthruster=on & pressure=low => thruster=nothrust')
    p.add_constraint('runthruster=off => thruster=nothrust')
    sat = SATSolver(p)

    thruster_model = {
        frozenset([T1.get_assignment('thrust')]) : {
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([T1.get_assignment('nothrust')]) : {
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([R1.get_assignment('on')]) : {
                frozenset([R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([R1.get_assignment('off')]) : {
                frozenset([R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
        
        frozenset([P3.get_assignment('high')]) : {},
        
        frozenset([P3.get_assignment('low')]) : {},
        }
    
    
    for key, value in thruster_model.items():
        assert_equal(fn(key,sat,value), solution_list[index])
        index+=1
        if value!={}:
            for key, value in value.items():
                assert_equal(fn(key,sat,value), solution_list[index])
                index+=1
                if value!={}:
                    for key, value in value.items():
                        assert_equal(fn(key,sat,value), solution_list[index])
                        index+=1
    return None

def check_unsatisfiability(fn):
    #Solution for Cases 1-26
    solution_list=[False, False, True, True, True, True, True, True, True, False, False, True, 
            True, False, True, True, True, True, False, True, True, False, True, True, True, True] 
    index=0
    p = Problem()
    T1 = p.add_variable('thruster', type='finite_domain', domain=['thrust', 'nothrust'])
    R1 = p.add_variable('runthruster', type='finite_domain', domain=['on', 'off'])
    P3 = p.add_variable('pressure', type='finite_domain', domain=['high', 'low'])
    p.add_constraint('runthruster=on & pressure=high => thruster=thrust')
    p.add_constraint('runthruster=on & pressure=low => thruster=nothrust')
    p.add_constraint('runthruster=off => thruster=nothrust')
    sat = SATSolver(p)

    thruster_model = {
        frozenset([T1.get_assignment('thrust')]) : {
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([T1.get_assignment('nothrust')]) : {
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([R1.get_assignment('on')]) : {
                frozenset([R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([R1.get_assignment('off')]) : {
                frozenset([R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
        
        frozenset([P3.get_assignment('high')]) : {},
        
        frozenset([P3.get_assignment('low')]) : {},
        }
    
    
    for key, value in thruster_model.items():
        assert_equal(fn(key,sat,value), solution_list[index])
        index+=1
        if value!={}:
            for key, value in value.items():
                assert_equal(fn(key,sat,value), solution_list[index])
                index+=1
                if value!={}:
                    for key, value in value.items():
                        assert_equal(fn(key,sat,value), solution_list[index])
                        index+=1
    return None

def check_prime_implicate_finder(fn):
    index=0
    p = Problem()
    T1 = p.add_variable('thruster', type='finite_domain', domain=['thrust', 'nothrust'])
    R1 = p.add_variable('runthruster', type='finite_domain', domain=['on', 'off'])
    P3 = p.add_variable('pressure', type='finite_domain', domain=['high', 'low'])
    p.add_constraint('runthruster=on & pressure=high => thruster=thrust')
    p.add_constraint('runthruster=on & pressure=low => thruster=nothrust')
    p.add_constraint('runthruster=off => thruster=nothrust')
    sat = SATSolver(p)

    solution_list=[([], [frozenset([T1.get_assignment('thrust')])], []), #Case 1
                   ([], [frozenset([T1.get_assignment('thrust'), R1.get_assignment('on')])], []), #Case 2
                   ([frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('high')])], [], []), #Case 3
                   ([frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('low')])], [], []), #Case 4
                   ([], [], [frozenset([T1.get_assignment('thrust'), R1.get_assignment('off')])]), #Case 5
                   ([frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('high')])], [], []), #Case 6
                   ([frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('low')])], [], []), #Case 7
                   ([frozenset([T1.get_assignment('thrust'), P3.get_assignment('high')])], [], []), #Case 8
                   ([frozenset([T1.get_assignment('thrust'), P3.get_assignment('low')])], [], []), #Case 9
                   ([], [frozenset([T1.get_assignment('nothrust')])], []), #Case 10
                   ([], [frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on')])], []), #Case 11
                   ([frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('high')])], [], []), #Case 12
                   ([frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('low')])], [], []), #Case 13
                   ([frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off')])], [], []), #Case 14
                   ([frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('high')])], [], []), #Case 15
                   ([frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('low')])], [], []), #Case 16
                   ([frozenset([T1.get_assignment('nothrust'), P3.get_assignment('high')])], [], []), #Case 17
                   ([frozenset([T1.get_assignment('nothrust'), P3.get_assignment('low')])], [], []), #Case 18
                   ([frozenset([R1.get_assignment('on')])], [], []), #Case 19
                   ([frozenset([R1.get_assignment('on'), P3.get_assignment('high')])], [], []), #Case 20
                   ([frozenset([R1.get_assignment('on'), P3.get_assignment('low')])], [], []), #Case 21
                   ([frozenset([R1.get_assignment('off')])], [], []), #Case 22
                   ([frozenset([R1.get_assignment('off'), P3.get_assignment('high')])], [], []), #Case 23
                   ([frozenset([R1.get_assignment('off'), P3.get_assignment('low')])], [], []), #Case 24
                   ([frozenset([P3.get_assignment('high')])], [], []), #Case 25
                   ([frozenset([P3.get_assignment('low')])], [], []) #Case 26
                   ]  

    #Our thruster_model from our problem is listed below:
    thruster_model = {
        frozenset([T1.get_assignment('thrust')]) : {
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('thrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('thrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([T1.get_assignment('nothrust')]) : {
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off')]) : {
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([T1.get_assignment('nothrust'), R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('high')]) : {},
            frozenset([T1.get_assignment('nothrust'), P3.get_assignment('low')]) : {},
            },
        
        frozenset([R1.get_assignment('on')]) : {
                frozenset([R1.get_assignment('on'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('on'), P3.get_assignment('low')]) : {},
                },
            frozenset([R1.get_assignment('off')]) : {
                frozenset([R1.get_assignment('off'), P3.get_assignment('high')]) : {},
                frozenset([R1.get_assignment('off'), P3.get_assignment('low')]) : {},
                },
        
        frozenset([P3.get_assignment('high')]) : {},
        
        frozenset([P3.get_assignment('low')]) : {},
        }
    
    
    for key, value in thruster_model.items():
        assert_equal(fn(sat, [(key, value)]), solution_list[index])
        index+=1
        if value!={}:
            for key, value in value.items():
                assert_equal(fn(sat, [(key, value)]), solution_list[index])
                index+=1
                if value!={}:
                    for key, value in value.items():
                        assert_equal(fn(sat, [(key, value)]), solution_list[index])
                        index+=1
    return None



"""
Various other utility functions
"""
def display_constraints(prob):
    print("Constraints:")
    try:
        from IPython.display import display, Latex
        for c in prob.constraints:
            display(Latex(c._repr_latex_()))
    except:
        for c in prob.constraints:
            print(c)
