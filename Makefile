
test_greedy_recursive:
	for t in test-greedy/*.in; do ./greedy_recursive.py $$t > sortida; diff -q test-greedy/`basename $$t .in`.ans sortida; done
	
test_greedy_iterative:
	for t in test-greedy/*.in; do ./greedy_iterative.py $$t > sortida; diff -q test-greedy/`basename $$t .in`.ans sortida; done

test_backtracking_recursive:
	for t in aqueductes/*.in; do ./backtracking_recursive.py $$t > sortida; diff -q aqueductes/`basename $$t .in`.ans sortida; done

test_backtracking_iterative:
	for t in aqueductes/*.in; do ./backtracking_iterative.py $$t > sortida; diff -q aqueductes/`basename $$t .in`.ans sortida; done

test_dynamic_programming_recursive:
	for t in aqueductes/*.in; do ./backtracking_recursive.py $$t > sortida; diff -q aqueductes/`basename $$t .in`.ans sortida; done

test_dynamic_programming_iterative:
	for t in aqueductes/*.in; do ./dynamic_programming_iterative.py $$t > sortida; diff -q aqueductes/`basename $$t .in`.ans sortida; done
