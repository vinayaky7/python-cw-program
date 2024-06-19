def km_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

# Example usage:
kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles")
