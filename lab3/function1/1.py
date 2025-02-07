def grams_to_ounces(grams):
    return 28.3495231 * grams

# Example usage:
grams = float(input("Enter the number of grams: "))
ounces = grams_to_ounces(grams)
print(f"{grams} grams = {ounces:.2f} ounces")
