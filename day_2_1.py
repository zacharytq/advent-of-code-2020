def parse_policy_line(line):
    line_list = line.split(' ')
    minimum = int(line_list[0].split('-')[0])
    maximum = int(line_list[0].split('-')[1])
    character = line_list[1][0]
    password = line_list[2]
    return dict([('min', minimum), ('max', maximum), ('char', character), ('password', password)])

def policy_dict_list(policy_list):
    dict_list = []
    for i, policy in enumerate(policy_list):
        dict_list.append(parse_policy_line(policy))
    return dict_list

def eval_policy(policy):
    return policy['min'] <= policy['password'].count(policy['char']) <= policy['max']

def count_passing(policy_list):
    count = 0
    for i, policy in enumerate(policy_list):
        if eval_policy(policy):
            count += 1
    return count

def count_passing_indices(policy_list):
    count = 0
    for i, policy in enumerate(policy_list):
        if eval_for_indices(policy):
            count += 1
    return count
    
def eval_for_indices(policy):
    one = policy['char'] == policy['password'][policy['min'] - 1]
    two = policy['char'] == policy['password'][policy['max'] - 1]
    if one and two:
        return False
    return one or two
