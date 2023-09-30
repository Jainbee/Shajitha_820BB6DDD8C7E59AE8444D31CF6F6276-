def linear_search_product(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices
# Example usage:
products = ["books", "pens", "paper", "books", "pencil", "books"]
target = "books"
result = linear_search_product(products, target)
#if the target value is not found
result = linear_search_product(products, target)
print(result)