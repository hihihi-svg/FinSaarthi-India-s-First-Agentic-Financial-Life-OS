import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from finsaarthi.tools.financial_calc import calculate_sip_for_goal, compare_tax_regimes

def test_sip_calculation():
    # Goal: 1Cr, 20 years, 12% returns
    sip = calculate_sip_for_goal(10000000, 20, 0.12)
    print(f"Monthly SIP for 1Cr in 20yrs at 12%: {sip}")
    assert sip > 0

def test_tax_comparison():
    # Salary 15L, Deductions 1.5L, HRA 50k, NPS 50k, Medical 25k
    result = compare_tax_regimes(1500000, 150000, 50000, 50000, 25000)
    print(f"Tax Comparison: {result}")
    assert 'old' in result
    assert 'new' in result
    assert 'savings' in result

if __name__ == "__main__":
    test_sip_calculation()
    test_tax_comparison()
    print("All tests passed!")
