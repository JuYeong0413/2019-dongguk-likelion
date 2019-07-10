from honey.post import Post
from honey import functions
# from honey.functions import sum_numbers
# from honey import functions as f
# from honey.functions import *
# import는 하나씩 해주는게 더 좋다

post = Post("개꿀", "밥더둑", 30)
post.delete()

print(functions.sum_numbers(5, 66))
