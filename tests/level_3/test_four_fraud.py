from functions.level_3.four_fraud import find_fraud_expenses

def test__find_fraud_expenses__return_true_with_fraud_chain_equal_to_in_chain_and_amount_less_than_max(sample_expenses_for_fraud_check):
    result = find_fraud_expenses(sample_expenses_for_fraud_check)
    assert len(result) == 3 

def test__find_fraud_expenses__return_true_with_transation_history_without_fraud(sample_expenses):
    result = find_fraud_expenses(sample_expenses)
    assert len(result) == 0

def test__find_fraud_expenses__return_true_with_with_fraud_chain_less_than_max_length(sample_expenses_for_fraud_check):
    result = find_fraud_expenses(sample_expenses_for_fraud_check[1:])
    assert len(result) == 0 
