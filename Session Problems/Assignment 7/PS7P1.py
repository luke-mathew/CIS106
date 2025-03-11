def main():
    principle = float(input("Enter principle amount: "))
    rate = float(input("Enter interest rate: "))

    total_interest = 0
    print(f"{'Year':<5}{'Beginning Balance':<20}{'Ending Balance':<20}")
    
    for year in range(1, 6):
        interest = principle * rate
        ending_balance = principle + interest
        total_interest += interest
        
        print(f"{year:<5}${principle:,.2f}       ${ending_balance:,.2f}")
        
        principle = ending_balance  # The ending balance becomes next year's principle

    print(f"\nTotal interest earned: ${total_interest:,.2f}")

main()

