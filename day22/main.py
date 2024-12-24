def mix_and_prune(secret_number, value_to_mix):
    secret_number ^= value_to_mix
    secret_number %= 16777216
    return secret_number

def generate_secret_number(initial_secret, steps=2000):
    secret_number = initial_secret
    for _ in range(steps):
        result = secret_number * 64
        secret_number = mix_and_prune(secret_number, result)

        result = secret_number // 32
        secret_number = mix_and_prune(secret_number, result)


        # result = secret_number * 2048
        # result = secret_number * 2048

        result = secret_number * 2048
        secret_number = mix_and_prune(secret_number, result)

    return secret_number

def read_initial_secrets(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

file_path = 'input.txt'

initial_secrets = read_initial_secrets(file_path)

total_sum = 0
for secret in initial_secrets:
    result = generate_secret_number(secret)
    total_sum += result

print(f"Total sum of the 2000th secret number for each buyer: {total_sum}")
