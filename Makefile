test_backtracking_recursive:
	clear
	./backtracking_recursive.py

test_greedy_iterative:
	clear
	./greedy_iterative.py

test_greedy_recursive:
	clear
	./greedy_recursive.py
	
test br:
	clear
	for t in testing/*.in; do ./backtracking_recursive.py $$t > sortida; diff -q testing/`basename $$t .in`.ans sortida; done
