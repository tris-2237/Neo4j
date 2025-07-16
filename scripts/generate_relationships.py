import random

with open('data/users_products_sample.csv', 'w') as f:
    f.write('user_id,product_id\n')
    for _ in range(10000):
        user_id = random.randint(1, 100)
        product_id = random.randint(1, 100)
        f.write(f"{user_id},{product_id}\n")
