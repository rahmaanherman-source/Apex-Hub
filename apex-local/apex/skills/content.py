from apex.models import local
def generateCopy(product_name,tone='bold'):
 return local.run(f'Write a {tone} short product description for: {product_name}. 2 sentences max.')
